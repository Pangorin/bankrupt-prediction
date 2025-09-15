# Ứng Dụng Dự Đoán Khả Năng Vỡ Nợ

Một ứng dụng web đơn giản sử dụng **Python Flask** và mô hình học máy **XGBoost** để dự đoán xác suất một cá nhân vỡ nợ dựa trên các thông tin tài chính cá nhân.

## 🎯 Mục Tiêu Dự Án

Mục tiêu chính của dự án này là:

  * Xây dựng một mô hình học máy để dự đoán rủi ro tín dụng.
  * Phát triển một ứng dụng web thân thiện với người dùng, cho phép nhập dữ liệu và nhận kết quả dự đoán ngay lập tức.
  * Áp dụng các kỹ thuật tiền xử lý dữ liệu và mô hình hóa tiên tiến để đạt được độ chính xác cao.

-----

## 🚀 Công Nghệ Sử Dụng

  * **Backend**: Python, Flask
  * **Machine Learning**: XGBoost, Scikit-learn, Pandas, Joblib
  * **Frontend**: HTML5, CSS3, Bootstrap 5

-----

## 📦 Cấu Trúc Thư Mục

Dự án được tổ chức theo cấu trúc sau:

```
.
├── app.py                     # Mã nguồn Flask cho backend
├── templates/
│   └── index.html             # Giao diện người dùng (HTML)
├── output_model/
│   ├── xgb_calibrated_model.joblib  # Mô hình XGBoost đã huấn luyện
│   ├── preprocessor.joblib          # Pipeline tiền xử lý dữ liệu
│   └── feature_names.csv            # Tên các đặc trưng được sử dụng
├── XGBoost_GiveMeSomeCredit.py  # Mã nguồn gốc để huấn luyện mô hình
├── cs-training.csv            # Dữ liệu gốc
└── README.md                  # File này
```

-----

## 🛠️ Hướng Dẫn Cài Đặt

### Bước 1: Clone kho lưu trữ

Sử dụng lệnh sau để tải dự án về máy của bạn:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

**Lưu ý:** Thay `your-username/your-repository-name.git` bằng thông tin kho lưu trữ của bạn.

### Bước 2: Tạo môi trường ảo (Virtual Environment)

Tạo và kích hoạt môi trường ảo để quản lý các thư viện:

```bash
# Đối với Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Đối với Windows
python -m venv venv
venv\Scripts\activate
```

### Bước 3: Cài đặt các thư viện cần thiết

Sử dụng `pip` để cài đặt tất cả các thư viện cần thiết:

```bash
pip install Flask pandas scikit-learn xgboost joblib
```

-----

## 🖥️ Hướng Dẫn Sử Dụng

1.  **Chạy ứng dụng web**: Mở terminal hoặc Command Prompt và chạy lệnh sau từ thư mục gốc của dự án:

    ```bash
    python app.py
    ```

2.  **Truy cập ứng dụng**: Mở trình duyệt web của bạn và truy cập vào địa chỉ:

    ```
    http://127.0.0.1:5000/
    ```

3.  **Dự đoán**: Nhập các thông tin tài chính cá nhân vào các trường trên giao diện và nhấn nút "Dự đoán" để xem kết quả.

-----

## 📄 Thông Tin Mô Hình

Mô hình được sử dụng trong dự án này là **XGBoost Calibrated Classifier**, đã được tinh chỉnh để cung cấp dự đoán xác suất chính xác. Các bước tiền xử lý dữ liệu, bao gồm xử lý giá trị thiếu và tạo đặc trưng mới (`Income_per_person`, `Debt_to_income_ratio`), được thực hiện tự động bởi một **pipeline** đã lưu.

-----

## 🤝 Đóng Góp

Đóng góp của bạn luôn được chào đón\! Nếu bạn có ý tưởng cải tiến, vui lòng:

1.  Fork (phân nhánh) kho lưu trữ này.
2.  Tạo một nhánh mới (`git checkout -b feature/your-feature-name`).
3.  Thực hiện các thay đổi của bạn.
4.  Commit các thay đổi (`git commit -m 'Add some feature'`).
5.  Push lên nhánh của bạn (`git push origin feature/your-feature-name`).
6.  Tạo một Pull Request.

-----

## 📜 Giấy Phép

Dự án này được cấp phép theo Giấy phép **MIT**. Xem tệp `LICENSE` để biết thêm chi tiết.
