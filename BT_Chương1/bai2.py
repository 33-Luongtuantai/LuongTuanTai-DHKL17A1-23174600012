
class ThiSinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def hien_thi_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hóa: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")

def nhap_danh_sach_thi_sinh():
    danh_sach = []
    so_luong = int(input("Nhập số lượng thí sinh: "))
    
    for _ in range(so_luong):
        ho_ten = input("Nhập họ tên thí sinh: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hóa: "))
        ts = ThiSinh(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach.append(ts)
    
    return danh_sach

def hien_thi_danh_sach_trung_tuyen(danh_sach, diem_chuan):
    # Lọc danh sách thí sinh có tổng điểm >= điểm chuẩn
    ds_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]
    
    ds_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    
    print(f"Danh sách thí sinh trúng tuyển (Điểm chuẩn: {diem_chuan}):")
    for ts in ds_trung_tuyen:
        ts.hien_thi_thong_tin()
        print("-----------------------------")

def main():
    danh_sach = nhap_danh_sach_thi_sinh()
    
    diem_chuan = float(input("Nhập điểm chuẩn vào trường: "))
    
    hien_thi_danh_sach_trung_tuyen(danh_sach, diem_chuan)

if __name__ == "__main__":
    main()
