from app import app, db
from models import Award

def update_award_gia_tri():
    with app.app_context():
        awards = Award.query.all()
        for award in awards:
            # Cập nhật giá trị tùy theo logic của bạn
            if award.ten_giai == "Giải đặc biệt":
                award.gia_tri = "03 Xe máy Honda Air Blade 125 - bản tiêu chuẩn"
            elif award.ten_giai == "Giải nhất":
                award.gia_tri = "15 Xe máy Honda Future 125Fi - bản tiêu chuẩn"
            elif award.ten_giai == "Giải nhì":
                award.gia_tri = "29 Máy tính bảng iPad Gen10 Wifi 5G 256GB"
            elif award.ten_giai == "Giải ba":
                award.gia_tri = "59 Apple Watch SE2 2024 GPS + Cellular"
            elif award.ten_giai == "Giải tư":
                award.gia_tri = "109 Phụ kiện Apple Tai nghe AirPods 2"    
            
        db.session.commit()
        print("Cập nhật giá trị giải thưởng thành công!")

if __name__ == "__main__":
    update_award_gia_tri()