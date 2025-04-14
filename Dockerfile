# Sử dụng Python 3.9 làm base image
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file requirements.txt
COPY requirements.txt .

# Cài đặt các dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Tạo thư mục temp_uploads nếu chưa tồn tại
RUN mkdir -p temp_uploads

# Mở port 5001
EXPOSE 5001

# Chạy ứng dụng
CMD ["python", "app.py"] 