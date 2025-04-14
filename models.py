from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ten_giai = db.Column(db.String(100), nullable=False)
    loai_phuong_thuc = db.Column(db.String(50))
    gia_tri = db.Column(db.String(250))
    da_duoc_phat = db.Column(db.Integer, default=0)

class Participant(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    ho_ten = db.Column(db.String(100), nullable=False)
    dia_chi = db.Column(db.String(200))
    ma_vung = db.Column(db.String(50))

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.String(20), db.ForeignKey('participant.id'), nullable=False)
    award_id = db.Column(db.Integer, db.ForeignKey('award.id'), nullable=False, index=True)
    thoi_gian = db.Column(db.DateTime, default=datetime.utcnow)

    participant = db.relationship('Participant', backref=db.backref('results', lazy=True))
    award = db.relationship('Award', backref=db.backref('results', lazy=True))
