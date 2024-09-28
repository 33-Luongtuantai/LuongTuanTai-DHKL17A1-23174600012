class DaGiac:
    def __init__(self, cac_canh):
        self.cac_canh = cac_canh
    
    def chu_vi(self):
        return sum(self.cac_canh)

    def dien_tich(self):
        raise NotImplementedError("Phương thức này nên được ghi đè bởi các lớp con")


class HinhBinhHanh(DaGiac):
    def __init__(self, day, chieu_cao, canh_ben):
        super().__init__([day, canh_ben, day, canh_ben])
        self.day = day
        self.chieu_cao = chieu_cao
        self.canh_ben = canh_ben
    
    def dien_tich(self):
        return self.day * self.chieu_cao


class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_rong, chieu_dai):
        super().__init__(chieu_rong, chieu_dai, chieu_rong)
    
    def dien_tich(self):
        return self.day * self.chieu_cao  # day là chieu_rong, chieu_cao là chieu_dai


class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
    
    def dien_tich(self):
        return self.day ** 2  # Cả chiều dài và chiều rộng đều bằng cạnh



hinh_binh_hanh = HinhBinhHanh(day=10, chieu_cao=5, canh_ben=7)
print(f"Chu vi Hình Bình Hành: {hinh_binh_hanh.chu_vi()}")
print(f"Diện tích Hình Bình Hành: {hinh_binh_hanh.dien_tich()}")

hinh_chu_nhat = HinhChuNhat(chieu_rong=10, chieu_dai=5)
print(f"Chu vi Hình Chữ Nhật: {hinh_chu_nhat.chu_vi()}")
print(f"Diện tích Hình Chữ Nhật: {hinh_chu_nhat.dien_tich()}")

hinh_vuong = HinhVuong(canh=5)
print(f"Chu vi Hình Vuông: {hinh_vuong.chu_vi()}")
print(f"Diện tích Hình Vuông: {hinh_vuong.dien_tich()}")
