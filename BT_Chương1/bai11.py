import math

# Lớp Tam Giác
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def kiem_tra_tam_giac(self):
        # Kiểm tra điều kiện tồn tại của tam giác
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def tinh_chu_vi(self):
        if self.kiem_tra_tam_giac():
            return self.a + self.b + self.c
        else:
            return "Không phải là tam giác hợp lệ."

    def tinh_dien_tich(self):
        if self.kiem_tra_tam_giac():
            p = self.tinh_chu_vi() / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            return "Không phải là tam giác hợp lệ."

# Lớp Tam Giác Vuông thừa kế từ Tam Giác
class TamGiacVuong(TamGiac):
    def kiem_tra_tam_giac_vuong(self):
        # Kiểm tra tam giác vuông bằng định lý Pythagoras
        canh = sorted([self.a, self.b, self.c])
        return math.isclose(canh[0]**2 + canh[1]**2, canh[2]**2)

    def tinh_dien_tich(self):
        if self.kiem_tra_tam_giac_vuong():
            return 0.5 * self.a * self.b
        else:
            return "Không phải tam giác vuông."

# Lớp Tam Giác Cân thừa kế từ Tam Giác
class TamGiacCan(TamGiac):
    def kiem_tra_tam_giac_can(self):
        return self.a == self.b or self.b == self.c or self.a == self.c

# Lớp Tam Giác Đều thừa kế từ Tam Giác Cân
class TamGiacDeu(TamGiacCan):
    def kiem_tra_tam_giac_deu(self):
        return self.a == self.b == self.c

# Chương trình chính để nhập thông tin và kiểm tra tam giác
def main():
    # Nhập thông tin tam giác
    print("Nhập các cạnh của tam giác:")
    a = float(input("Cạnh a: "))
    b = float(input("Cạnh b: "))
    c = float(input("Cạnh c: "))

    # Tạo đối tượng Tam Giác
    tam_giac = TamGiac(a, b, c)

    # Kiểm tra và hiển thị loại tam giác
    if tam_giac.kiem_tra_tam_giac():
        print(f"Chu vi tam giác: {tam_giac.tinh_chu_vi()}")
        print(f"Diện tích tam giác: {tam_giac.tinh_dien_tich()}")

        # Kiểm tra tam giác vuông
        tam_giac_vuong = TamGiacVuong(a, b, c)
        if tam_giac_vuong.kiem_tra_tam_giac_vuong():
            print("Đây là tam giác vuông.")
            print(f"Diện tích tam giác vuông: {tam_giac_vuong.tinh_dien_tich()}")
        else:
            print("Không phải tam giác vuông.")

        # Kiểm tra tam giác cân
        tam_giac_can = TamGiacCan(a, b, c)
        if tam_giac_can.kiem_tra_tam_giac_can():
            print("Đây là tam giác cân.")
        
        # Kiểm tra tam giác đều
        tam_giac_deu = TamGiacDeu(a, b, c)
        if tam_giac_deu.kiem_tra_tam_giac_deu():
            print("Đây là tam giác đều.")
        else:
            print("Không phải tam giác đều.")
    else:
        print("Đây không phải là tam giác hợp lệ.")

if __name__ == "__main__":
    main()
