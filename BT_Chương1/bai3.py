class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau
        if not self.hopLe():
            raise ValueError("Mẫu số phải khác 0!")
    
    def hopLe(self):
        return self.mau != 0
    
    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        if not self.hopLe():
            raise ValueError("Mẫu số phải khác 0!")
    
    def inPhanSo(self):
        if self.mau == 1:
            print(f"Phân số là: {self.tu}")
        else:
            print(f"Phân số là: {self.tu}/{self.mau}")


try:
    phanso = PhanSo()  
    phanso.nhap()  
    phanso.inPhanSo()  
except ValueError :
    print("Mẫu số phải khác 0!")
