class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def hien_thi(self):
        print(f"Ngày: {self.ngay}/{self.thang}/{self.nam}")

    def next_day(self):
        ngay_cuoi_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Kiểm tra năm nhuận
        if (self.nam % 400 == 0) or (self.nam % 4 == 0 and self.nam % 100 != 0):
            ngay_cuoi_thang[1] = 29  # Tháng 2 có 29 ngày trong năm nhuận

        self.ngay += 1

        if self.ngay > ngay_cuoi_thang[self.thang - 1]:
            self.ngay = 1
            self.thang += 1


# Sử dụng lớp Date
d = Date(31, 12, 2023)  # Khởi tạo ngày 31 tháng 12 năm 2023
d.hien_thi()  # In ngày hiện tại
d.next_day()  # Tính ngày tiếp theo
d.hien_thi()  # In ngày sau khi tính ngày tiếp theo
