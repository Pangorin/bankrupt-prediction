import os
import joblib
import pandas as pd
from flask import Flask, render_template, request

# Create a Flask app instance
app = Flask(__name__)

# Load the trained model and preprocessor at the start
try:
    model_path = os.path.join("output_model", "xgb_calibrated_model.joblib")
    preprocessor_path = os.path.join("output_model", "preprocessor.joblib")
    feature_names_path = os.path.join("output_model", "feature_names.csv")
    
    # Check if files exist before loading
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
    if not os.path.exists(preprocessor_path):
        raise FileNotFoundError(f"Preprocessor file not found at: {preprocessor_path}")
    if not os.path.exists(feature_names_path):
        raise FileNotFoundError(f"Feature names file not found at: {feature_names_path}")

    calibrated_clf = joblib.load(model_path)
    preprocessor = joblib.load(preprocessor_path)
    feature_names_df = pd.read_csv(feature_names_path, header=None)
    feature_names = feature_names_df.iloc[:, 0].tolist()

    print("Models and data loaded successfully!")
except Exception as e:
    print(f"Error loading models or data: {e}")
    # Exit the application if loading fails
    exit()

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    prediction_result = None
    form_data = {}
    
    # Map form fields to the correct feature names
    form_to_feature_map = {
        "RevolvingUtilizationOfUnsecuredLines": "RevolvingUtilizationOfUnsecuredLines",
        "age": "age",
        "NumberOfTime30-59DaysPastDueNotWorse": "NumberOfTime30-59DaysPastDueNotWorse",
        "DebtRatio": "DebtRatio",
        "MonthlyIncome": "MonthlyIncome",
        "NumberOfOpenCreditLinesAndLoans": "NumberOfOpenCreditLinesAndLoans",
        "NumberOfTimes90DaysLate": "NumberOfTimes90DaysLate",
        "NumberRealEstateLoansOrLines": "NumberRealEstateLoansOrLines",
        "NumberOfTime60-89DaysPastDueNotWorse": "NumberOfTime60-89DaysPastDueNotWorse",
        "NumberOfDependents": "NumberOfDependents"
    }
    
    if request.method == "POST":
        try:
            # Get data from the form and store it
            for form_field, feature_name in form_to_feature_map.items():
                form_data[feature_name] = float(request.form.get(form_field, 0))
            
            # Create a DataFrame with the correct column order from feature_names
            input_df = pd.DataFrame(columns=feature_names)
            
            # Append the data
            input_df.loc[0] = [form_data.get(col, 0) for col in feature_names]
            
            # Re-engineering features from the original script
            input_df["MonthlyIncome_missing"] = input_df["MonthlyIncome"].apply(lambda x: 1 if pd.isnull(x) or x == 0 else 0)
            input_df["NumberOfDependents_missing"] = input_df["NumberOfDependents"].apply(lambda x: 1 if pd.isnull(x) or x == 0 else 0)
            
            input_df["MonthlyIncome_fillna"] = input_df["MonthlyIncome"].fillna(0)
            input_df["NumberOfDependents_fillna"] = input_df["NumberOfDependents"].fillna(0) + 1
            
            input_df["Income_per_person"] = input_df["MonthlyIncome_fillna"] / input_df["NumberOfDependents_fillna"]
            input_df["Debt_to_income_ratio"] = input_df["DebtRatio"] * input_df["MonthlyIncome_fillna"]
            
            # Ensure the input has the same columns as the preprocessor expects
            input_df = input_df[preprocessor.feature_names_in_]
            
            # Preprocessing and Prediction
            processed_data = preprocessor.transform(input_df)
            prediction_proba = calibrated_clf.predict_proba(processed_data)[:, 1][0]
            
            prediction_result = f"Xác suất vỡ nợ: {prediction_proba * 100:.2f}%"

        except Exception as e:
            prediction_result = f"Đã xảy ra lỗi: {e}"
            print(f"Error during prediction: {e}")

    return render_template("index.html", prediction_result=prediction_result, form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)