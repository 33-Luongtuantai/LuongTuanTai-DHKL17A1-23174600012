class Hinhchunhat:
    def __init__(self,chieudai,chieurong):
        self.chieudai=chieudai
        self.chieurong=chieurong
    def nhap_kich_thuoc(self):
        self.chieudai=float(input("nhập chiều dài:"))
        self.chieurong=float(input("nhập chiều rộng:"))
    def tinh_chu_vi(self):
        return 2 * (self.chieudai + self.chieurong)
    def tinh_dien_tich(self):
        return self.chieudai * self.chieurong
    def hien_thi_thong_tin(self):
        print(f"Chiều dài: {self.chieudai}")
        print(f"Chiều rộng: {self.chieurong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

def main():
    hcn = Hinhchunhat(0, 0)
    hcn.nhap_kich_thuoc()
    hcn.hien_thi_thong_tin()
if __name__=="__main__":
    main()