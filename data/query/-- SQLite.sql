-- SQLite
INSERT INTO award (id, ten_giai, loai_phuong_thuc, gia_tri, da_duoc_phat)
VALUES (1, "Vé du lịch", "Quay tự động", "120 vé du lịch Thái Lan - Vùng Đồng Bằng Sông Cửu Long
", 0);


INSERT INTO award (id, ten_giai, loai_phuong_thuc, gia_tri, da_duoc_phat)
VALUES (1, "Vé du lịch", "Quay tự động", "30 vé du lịch Thái lan - Vùng Đông Nam Bộ, Miền Trung, Tây Nguyên
", 0);


--- UPDATE

UPDATE award
SET gia_tri = '30 vé du lịch Thái lan - Vùng Đông Nam Bộ, Miền Trung, Tây Nguyên
'
WHERE id = 1;



DELETE FROM award WHERE id = 1;
DELETE FROM award WHERE id = 2;
DELETE FROM award WHERE id = 3;
DELETE FROM award WHERE id = 4;
DELETE FROM award WHERE id = 5;
DELETE FROM award WHERE id = 6;
DELETE FROM award WHERE id = 7;
DELETE FROM award WHERE id = 8;