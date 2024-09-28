import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def hien_thi(self):
        return f"({self.x}, {self.y})"

# Lớp Elip thừa kế từ lớp Điểm
class Elip(Diem):
    def __init__(self, x, y, ban_truc_lon, ban_truc_nho):
        super().__init__(x, y)  
        self.ban_truc_lon = ban_truc_lon
        self.ban_truc_nho = ban_truc_nho

    def tinh_dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_nho

    def hien_thi_thong_tin(self):
        print(f"Elip tại tọa độ: {self.hien_thi()}")
        print(f"Bán trục lớn: {self.ban_truc_lon}")
        print(f"Bán trục nhỏ: {self.ban_truc_nho}")
        print(f"Diện tích elip: {self.tinh_dien_tich()}")

# Lớp Đường Tròn thừa kế từ lớp Elip
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)  

    def tinh_dien_tich(self):
        return math.pi * self.ban_truc_lon**2  

    def hien_thi_thong_tin(self):
        print(f"Đường tròn tại tọa độ: {self.hien_thi()}")
        print(f"Bán kính: {self.ban_truc_lon}")
        print(f"Diện tích đường tròn: {self.tinh_dien_tich()}")


def main():
    print("Nhập thông tin cho elip:")
    x = float(input("Nhập tọa độ x của elip: "))
    y = float(input("Nhập tọa độ y của elip: "))
    ban_truc_lon = float(input("Nhập bán trục lớn của elip: "))
    ban_truc_nho = float(input("Nhập bán trục nhỏ của elip: "))

    elip = Elip(x, y, ban_truc_lon, ban_truc_nho)
    elip.hien_thi_thong_tin()


    print("\nNhập thông tin cho đường tròn:")
    x = float(input("Nhập tọa độ x của đường tròn: "))
    y = float(input("Nhập tọa độ y của đường tròn: "))
    ban_kinh = float(input("Nhập bán kính của đường tròn: "))

    duong_tron = DuongTron(x, y, ban_kinh)
    duong_tron.hien_thi_thong_tin()

if __name__ == "__main__":
    main()
