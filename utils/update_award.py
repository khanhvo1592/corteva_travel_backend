from app import app, db
from models import Award

def update_award_gia_tri():
    with app.app_context():
        awards = Award.query.all()
        for award in awards:
            # Cập nhật giá trị tùy theo logic của bạn
            if award.ten_giai == "Vé du lịch":
                award.gia_tri = "150 vé du lịch Thái Lan"
            
        db.session.commit()
        print("Cập nhật giá trị giải thưởng thành công!")

if __name__ == "__main__":
    update_award_gia_tri()