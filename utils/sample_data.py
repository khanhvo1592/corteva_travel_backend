from flask import Flask
from models import db, Award, Participant, Result
from datetime import datetime, timedelta, timezone
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def add_sample_data():
    # Xóa dữ liệu cũ
    Result.query.delete()
    Participant.query.delete()
    Award.query.delete()
    db.session.commit()

    # Thêm giải thưởng
    awards = [
        Award(id=1, ten_giai="Giải tư", loai_phuong_thuc="Quay tự động", gia_tri="Tai nghe AirPods 2"),
        Award(id=2, ten_giai="Giải ba", loai_phuong_thuc="Quay tự động", gia_tri="Apple Watch SE 2 2024 GPS + Cellular"),
        Award(id=3, ten_giai="Giải nhì", loai_phuong_thuc="Quay tự động", gia_tri="Máy tính bảng iPad Gen 10 Wifi 5G 256GB"),
        Award(id=4, ten_giai="Giải nhất", loai_phuong_thuc="Quay lồng cầu", gia_tri="xe Future Neo 125Fi"),
        Award(id=5, ten_giai="Giải đặc biệt", loai_phuong_thuc="Quay lồng cầu", gia_tri="Xe máy Honda Air Blade 125")
    ]
    db.session.add_all(awards)
    db.session.commit()

    # Thêm người tham gia
    participants = [
        Participant(id="12345", ho_ten="Nguyễn Văn A", dia_chi="Cần Thơ"),
        Participant(id="67890", ho_ten="Trần Thị B", dia_chi="Kiên Giang"),
        Participant(id="11111", ho_ten="Lê Văn C", dia_chi="An Giang"),
        Participant(id="22222", ho_ten="Phạm Thị D", dia_chi="Đồng Tháp"),
        Participant(id="33333", ho_ten="Huỳnh Văn E", dia_chi="Vĩnh Long")
    ]
    db.session.add_all(participants)
    db.session.commit()

    # Thêm một số kết quả mẫu
    now = datetime.now(timezone.utc)
    for i in range(10):
        participant = random.choice(participants)
        award = random.choice(awards)
        result_time = now - timedelta(minutes=random.randint(1, 60))
        result = Result(participant_id=participant.id, award_id=award.id, thoi_gian=result_time)
        db.session.add(result)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_sample_data()
    print("Dữ liệu mẫu đã được thêm vào database.")
