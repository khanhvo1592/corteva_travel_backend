from flask import Blueprint, request, jsonify
from extensions import db
from models import Award

award_bp = Blueprint('award', __name__)

@award_bp.route('/api/awards', methods=['GET'])
def get_awards():
    try:
        awards = Award.query.all()
        awards_list = [{
            'id': award.id,
            'ten_giai': award.ten_giai,
            'loai_phuong_thuc': award.loai_phuong_thuc,
            'gia_tri': award.gia_tri,
            'da_duoc_phat': award.da_duoc_phat
        } for award in awards]
        return jsonify({'success': True, 'data': awards_list}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@award_bp.route('/api/awards/<int:award_id>', methods=['PUT'])
def update_award(award_id):
    try:
        award = Award.query.get(award_id)
        if not award:
            return jsonify({'success': False, 'message': 'Không tìm thấy giải thưởng'}), 404

        data = request.json
        if 'ten_giai' in data:
            award.ten_giai = data['ten_giai']
        if 'loai_phuong_thuc' in data:
            award.loai_phuong_thuc = data['loai_phuong_thuc']
        if 'gia_tri' in data:
            award.gia_tri = data['gia_tri']
        if 'da_duoc_phat' in data:
            award.da_duoc_phat = data['da_duoc_phat']

        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Cập nhật giải thưởng thành công',
            'data': {
                'id': award.id,
                'ten_giai': award.ten_giai,
                'loai_phuong_thuc': award.loai_phuong_thuc,
                'gia_tri': award.gia_tri,
                'da_duoc_phat': award.da_duoc_phat
            }
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@award_bp.route('/api/awards/init', methods=['POST'])
def init_awards():
    try:
        # Xóa tất cả dữ liệu cũ
        Award.query.delete()
        
        # Dữ liệu mẫu
        sample_awards = [
            {
                'ten_giai': 'Giải tư',
                'loai_phuong_thuc': 'Quay tự động',
                'gia_tri': '109 Phụ kiện Apple Tai nghe AirPods 2',
                'da_duoc_phat': False
            },
            {
                'ten_giai': 'Giải ba',
                'loai_phuong_thuc': 'Quay tự động',
                'gia_tri': '59 Apple Watch SE 2 2024 GPS + Cellular',
                'da_duoc_phat': False
            },
            {
                'ten_giai': 'Giải nhì',
                'loai_phuong_thuc': 'Quay tự động',
                'gia_tri': '29 Máy tính bảng iPad Gen10 Wifi 5G 256GB',
                'da_duoc_phat': False
            },
            {
                'ten_giai': 'Giải nhất',
                'loai_phuong_thuc': 'Quay lồng cầu',
                'gia_tri': '15 Xe máy Honda Future 125Fi - bản tiêu chuẩn',
                'da_duoc_phat': False
            },
            {
                'ten_giai': 'Giải đặc biệt',
                'loai_phuong_thuc': 'Quay lồng cầu',
                'gia_tri': '03 Xe máy Honda Air Blade 125 - bản tiêu chuẩn',
                'da_duoc_phat': False
            }
        ]

        for award_data in sample_awards:
            award = Award(**award_data)
            db.session.add(award)

        db.session.commit()
        return jsonify({'success': True, 'message': 'Khởi tạo dữ liệu giải thưởng thành công'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500