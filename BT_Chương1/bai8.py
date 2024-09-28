
class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def hien_thi(self):
        return f"{self.ngay}/{self.thang}/{self.nam}"


class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh  
        self.ngay_vao_cong_ty = ngay_vao_cong_ty  

    def hien_thi_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngày sinh: {self.ngay_sinh.hien_thi()}")
        print(f"Ngày vào công ty: {self.ngay_vao_cong_ty.hien_thi()}")


def quan_ly_nhan_vien():
    danh_sach_nhan_vien = []
    
    so_luong_nv = int(input("Nhập số lượng nhân viên: "))
    
    for i in range(so_luong_nv):
        ho_ten = input(f"Nhập họ tên nhân viên {i + 1}: ")
        

        ngay = int(input("Nhập ngày sinh: "))
        thang = int(input("Nhập tháng sinh: "))
        nam = int(input("Nhập năm sinh: "))
        ngay_sinh = Date(ngay, thang, nam)
        

        ngay = int(input("Nhập ngày vào công ty: "))
        thang = int(input("Nhập tháng vào công ty: "))
        nam = int(input("Nhập năm vào công ty: "))
        ngay_vao_cong_ty = Date(ngay, thang, nam)
        

        nv = Employee(ho_ten, ngay_sinh, ngay_vao_cong_ty)
        danh_sach_nhan_vien.append(nv)
    

    print("\nDanh sách nhân viên:")
    for nv in danh_sach_nhan_vien:
        nv.hien_thi_thong_tin()
        print("---------")

quan_ly_nhan_vien()
