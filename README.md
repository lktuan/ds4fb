# **ds4fb**

Repo for holding my code along with the book: Data Science in Finance & Banking
Code của tôi theo cuốn sách "Khoa học dữ liệu trong lĩnh vực Tài chính - Ngân hàng"

![Ảnh bìa sách, nguồn Tiki](book_cover.png "Book cover")

## Yêu cầu hệ thống

- Python >= 3.8
- Git

## Cài đặt và sử dụng

1. Clone repository:

```bash
git clone https://github.com/lktuan/ds4fb.git
cd ds4fb
```

1. Tạo và kích hoạt môi trường ảo:
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

3. Cài đặt project và dependencies:

```bash
# Cài đặt các dependencies
pip install -r requirements.txt

# # Cài đặt Jupyter Notebook extensions để format code trực tiếp trong notebook
# pip install jupyter_contrib_nbextensions
# jupyter contrib nbextension install --user
```

4. Thiết lập pre-commit hooks:

```bash
pre-commit install
```

5. Đăng ký Kernel của `.venv` cho Jupyter nếu chưa có

```bash
python -m ipykernel install --user --name=ds4fb
```

6. Tạo data

credit dataset
```bash
python .\data\generator\credit_data_gen.py
```

## Development

### Code Style

Project này sử dụng:
- black cho code formatting
- isort cho import sorting
- flake8 cho code linting

Các tools này được tự động chạy thông qua pre-commit hooks mỗi khi commit.

Để chạy format manually:

```bash
# Format toàn bộ project
black .
isort .

# Kiểm tra lỗi
flake8
```

## Dependencies chính

- pandas >= 2.2.0
- numpy >= 1.26.0
- scikit-learn >= 1.4.0
- scipy >= 1.12.0
- statsmodels >= 0.14.1
- pytorch >= 2.2.0
- tensorflow >= 2.15.0
