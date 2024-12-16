import pandas as pd
import numpy as np
file_path = '/Users/macos/Documents/diem_hoc_phan.csv'  
data_0 = pd.read_csv(file_path)
data=np.array(data_0)
def grade_to_letter(score):
    if 8.5 <= score <= 10:
        return 'A'
    elif 8.0 <= score < 8.5:
        return 'B+'
    elif 7.0 <= score < 8.0:
        return 'B'
    elif 6.5 <= score < 7.0:
        return 'C+'
    elif 5.5 <= score < 6.5:
        return 'C'
    elif 5.0 <= score < 5.5:
        return 'D+'
    elif 4.0 <= score < 5.0:
        return 'D'
    else:
        return 'F'

# Áp dụng hàm chuyển đổi cho từng học phần (HP1, HP2, HP3) của mỗi sinh viên
def convert_grades_to_letters(data):
    # Tạo một mảng mới để chứa điểm chữ cho từng học phần
    grades = np.array([data[:, 2], data[:, 3], data[:, 4]])  # HP1, HP2, HP3
    grades_letters = np.vectorize(grade_to_letter)(grades)  # Áp dụng hàm grade_to_letter cho từng phần tử

    return grades_letters.T  # Trả về kết quả đã chuyển đổi

# Chuyển đổi điểm số thành điểm chữ cho từng học phần
grades_letters = convert_grades_to_letters(data)

# In kết quả
print("Điểm chữ cho từng học phần:")
for i, student in enumerate(data[:, 1], start=1):  # In tên sinh viên
    print(f"{student}: HP1 = {grades_letters[i-1][0]}, HP2 = {grades_letters[i-1][1]}, HP3 = {grades_letters[i-1][2]}")

# Lấy dữ liệu điểm của các học phần (HP1, HP2, HP3)
hp1 = data[:, 2].astype(float)  # Điểm HP1
hp2 = data[:, 3].astype(float)  # Điểm HP2
hp3 = data[:, 4].astype(float)  # Điểm HP3

def calculate_stats(grades):
    total = np.sum(grades)  # Tổng điểm
    mean = np.mean(grades)  # Trung bình
    std_dev = np.std(grades)  # Độ lệch chuẩn
    return total, mean, std_dev

# Tính toán cho từng học phần
hp1_total, hp1_mean, hp1_std_dev = calculate_stats(hp1)
hp2_total, hp2_mean, hp2_std_dev = calculate_stats(hp2)
hp3_total, hp3_mean, hp3_std_dev = calculate_stats(hp3)

# In kết quả
print("Học phần 1 (HP1):")
print(f"Tổng điểm: {hp1_total:.2f}, Trung bình: {hp1_mean:.2f}, Độ lệch chuẩn: {hp1_std_dev:.2f}\n")

print("Học phần 2 (HP2):")
print(f"Tổng điểm: {hp2_total:.2f}, Trung bình: {hp2_mean:.2f}, Độ lệch chuẩn: {hp2_std_dev:.2f}\n")

print("Học phần 3 (HP3):")
print(f"Tổng điểm: {hp3_total:.2f}, Trung bình: {hp3_mean:.2f}, Độ lệch chuẩn: {hp3_std_dev:.2f}")

def grade_to_letter(grade):
    if 8.5 <= grade <= 10:
        return 'A'
    elif 8.0 <= grade < 8.5:
        return 'B+'
    elif 7.0 <= grade < 8.0:
        return 'B'
    elif 6.5 <= grade < 7.0:
        return 'C+'
    elif 5.5 <= grade < 6.5:
        return 'C'
    elif 5.0 <= grade < 5.5:
        return 'D+'
    elif 4.0 <= grade < 5.0:
        return 'D'
    else:
        return 'F'

# Hàm đếm số sinh viên đạt điểm chữ cho từng học phần
def count_grade_letters(grades):
    grade_counts = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'F': 0}
    
    for grade in grades:
        letter = grade_to_letter(grade)
        grade_counts[letter] += 1
    
    return grade_counts

# Tách điểm của các học phần
hp1 = data[:, 2].astype(float)  # Điểm HP1
hp2 = data[:, 3].astype(float)  # Điểm HP2
hp3 = data[:, 4].astype(float)  # Điểm HP3

# Đếm số sinh viên đạt điểm chữ cho từng học phần
hp1_grade_counts = count_grade_letters(hp1)
hp2_grade_counts = count_grade_letters(hp2)
hp3_grade_counts = count_grade_letters(hp3)

# In kết quả
print("Điểm chữ của học phần 1 (HP1):", hp1_grade_counts)
print("Điểm chữ của học phần 2 (HP2):", hp2_grade_counts)
print("Điểm chữ của học phần 3 (HP3):", hp3_grade_counts)