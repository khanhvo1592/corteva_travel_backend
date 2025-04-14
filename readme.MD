# Backend ứng dụng quay số may mắn

## Giới thiệu
Dự án này là một ứng dụng quay số được xây dựng bằng Flask, cho phép người dùng tham gia vào các giải thưởng và quay số để chọn người thắng cuộc. Ứng dụng hỗ trợ tải lên danh sách người tham gia từ file Excel, quản lý giải thưởng, và thực hiện quay số tự động hoặc thủ công.

## Công nghệ sử dụng
- **Flask**: Framework web cho Python.
- **SQLAlchemy**: ORM cho Python để tương tác với cơ sở dữ liệu.
- **SQLite**: Cơ sở dữ liệu nhẹ để lưu trữ dữ liệu.
- **OpenPyXL**: Thư viện để đọc và ghi file Excel.
- **Flask-CORS**: Thư viện để xử lý CORS (Cross-Origin Resource Sharing).

## Cài đặt

### Yêu cầu
- Python 3.x

### Cài đặt các thư viện cần thiết
```bash
pip install Flask Flask-CORS Flask-Migrate openpyxl
```

### Cấu hình cơ sở dữ liệu
1. Tạo file `database.db` trong thư mục gốc của dự án.
2. Chạy lệnh sau để tạo các bảng trong cơ sở dữ liệu:
```bash
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```

### Các API chính

- **Lấy danh sách giải thưởng**
  - **Endpoint**: `/api/awards`
  - **Phương thức**: GET
  - **Mô tả**: Lấy danh sách tất cả các giải thưởng.

- **Quay số tự động**
  - **Endpoint**: `/api/quay-so`
  - **Phương thức**: POST
  - **Body**: 
    ```json
    {
      "awardId": "ID của giải thưởng"
    }
    ```
  - **Mô tả**: Quay số để chọn người thắng cuộc cho giải thưởng đã chỉ định.

- **Quay số thủ công**
  - **Endpoint**: `/api/quay-so-manual`
  - **Phương thức**: POST
  - **Body**: 
    ```json
    {
      "awardId": "ID của giải thưởng",
      "inputNumber": "Số tham gia"
    }
    ```
  - **Mô tả**: Quay số thủ công cho người tham gia với số đã nhập.

- **Tải lên danh sách người tham gia**
  - **Endpoint**: `/api/participants/upload`
  - **Phương thức**: POST
  - **Body**: File Excel chứa danh sách người tham gia.
  - **Mô tả**: Tải lên file Excel để thêm hoặc cập nhật người tham gia.

- **Lấy kết quả quay số**
  - **Endpoint**: `/api/results`
  - **Phương thức**: GET
  - **Query Parameters**: 
    - `search`: Tìm kiếm theo tên hoặc địa chỉ.
    - `award`: Lọc theo ID giải thưởng.
  - **Mô tả**: Lấy danh sách kết quả quay số.

## Ghi chú
- Đảm bảo rằng bạn đã cài đặt tất cả các thư viện cần thiết trước khi chạy ứng dụng.
- Kiểm tra logs trong terminal để theo dõi các hoạt động và lỗi của ứng dụng.

## Tài liệu tham khảo
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [OpenPyXL Documentation](https://openpyxl.readthedocs.io/en/stable/)

## Liên hệ
Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ với tôi qua email: [your_email@example.com].



# update ma_vung
I see the issue - there's a conflict with the database migrations. The error shows that the table `award` already exists when the migration is trying to create it. This suggests that the database tables were created but the migration history is not in sync.

Let's fix this by following these steps:

1. First, let's remove the existing database file:
```bash
rm instance/database.db
```

2. Then, remove the migrations folder to start fresh:
```bash
rm -rf migrations/
```

3. Now, let's reinitialize the migrations:
```bash
flask db init
```

4. Create a new migration that includes all our tables including the new `ma_vung` column:
```bash
flask db migrate -m "initial migration"
```

5. Finally, apply the migration:
```bash
flask db upgrade
```

This should resolve the migration conflict and properly set up your database with all the tables, including the new `ma_vung` column in the `participant` table.

Would you like me to help you with any of these steps or do you need clarification on anything?
