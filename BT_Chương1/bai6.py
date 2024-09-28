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
    
    def hienThi(self): # print(in ra nội dung ngăn xếp)
        print("Nội dung ngăn xếp:", self.nganxep)

ngan_xep = NganXep(0)  
ngan_xep.them(4)
ngan_xep.them(20)
ngan_xep.hienThi()

ngan_xep.layRa()
ngan_xep.hienThi()

print("Ngăn xếp rỗng?", ngan_xep.isRong())
print("Ngăn xếp đầy?", ngan_xep.isDay())

