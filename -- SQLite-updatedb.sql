-- SQLite
SELECT id, ten_giai, loai_phuong_thuc, gia_tri, da_duoc_phat
FROM award;

UPDATE award
SET gia_tri = '109 Phụ kiện Apple Tai nghe AirPods 2'
WHERE id = 1;

UPDATE award
SET gia_tri = '59 Apple Watch SE 2 2024 GPS + Cellular'
WHERE id = 2;

UPDATE award
SET gia_tri = '03 Xe máy Honda Air Blade 125 - bản tiêu chuẩn'
WHERE id = 3;


UPDATE award
SET gia_tri = '15 xe máy Honda Future 125Fi - bản tiêu chuẩn'
WHERE id = 4;

UPDATE award
SET gia_tri = '03 xe máy Honda Air Blade 125 - bản tiêu chuẩn'
WHERE id = 5;
