import numpy as np


with open('/Users/macos/Documents/efficiency.txt', 'r') as file:
    hiệu_suất = [int(line.strip()) for line in file]

with open('/Users/macos/Documents/shifts.txt', 'r') as file:
    ca_làm_việc = [line.strip() for line in file]


np_ca_làm_việc = np.array(ca_làm_việc)
print("Kiểu dữ liệu của np_ca_làm_việc:", np_ca_làm_việc.dtype)

np_hiệu_suất = np.array(hiệu_suất)
print("Kiểu dữ liệu của np_hiệu_suất:", np_hiệu_suất.dtype)

hiệu_suất_ca_sáng = np_hiệu_suất[np_ca_làm_việc == 'Morning']
hiệu_suất_trung_bình_ca_sáng = hiệu_suất_ca_sáng.mean()
print("Hiệu suất sản xuất trung bình của ca 'Morning':", hiệu_suất_trung_bình_ca_sáng)

hiệu_suất_ca_khác = np_hiệu_suất[np_ca_làm_việc != 'Morning']
hiệu_suất_trung_bình_ca_khác = hiệu_suất_ca_khác.mean()
print("Hiệu suất sản xuất trung bình của các ca khác (không phải 'Morning'):", hiệu_suất_trung_bình_ca_khác)
