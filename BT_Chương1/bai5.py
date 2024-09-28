class NganXep:
    def __init__(self, succhua):
        self.succhua = succhua
        self.nganxep = []
    

    def isRong(self):
        return len(self.nganxep) == 0

    def isDay(self):
        return len(self.nganxep) == self.succhua
    
    def them(self, phantu):
        if self.isDay():
            print("Ngăn xếp đã đầy. Không thể thêm!")
        else:
            self.nganxep.append(phantu)
    
    def layRa(self):
        if self.isRong():
            print("Ngăn xếp rỗng. Không thể lấy!")
        else:
            return self.nganxep.pop()
    
    def hienThi(self):
        print("Nội dung ngăn xếp:", self.nganxep)
    
    def demSoPhanTu(self): #hàm count
        return len(self.nganxep)

ngan_xep = NganXep(5)  # Ngăn xếp có sức chứa là 5
ngan_xep.them(10.5)
ngan_xep.them(20.3)
ngan_xep.hienThi()

print("Số phần tử trong ngăn xếp:", ngan_xep.demSoPhanTu())

ngan_xep.layRa()
ngan_xep.hienThi()

print("Số phần tử trong ngăn xếp sau khi lấy ra:", ngan_xep.demSoPhanTu())
