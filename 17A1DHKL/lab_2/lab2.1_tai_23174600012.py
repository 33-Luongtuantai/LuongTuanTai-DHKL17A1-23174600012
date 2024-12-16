import numpy as np

# 1. Tạo Dữ Liệu Mô Phỏng Nhiệt Độ
# Giả lập nhiệt độ cho 30 ngày trong tháng
np.random.seed(42)  # Đặt seed để kết quả tái lặp
temperatures = np.round(np.random.uniform(15, 35, 30), 2)  # Nhiệt độ từ 15 đến 35, làm tròn 2 chữ số
print("Nhiệt độ trong tháng (°C):", temperatures)

# Tính nhiệt độ trung bình
average_temp = np.round(np.mean(temperatures), 2)
print("Nhiệt độ trung bình trong tháng là:", average_temp, "°C")

# 2. Phân Tích Xu Hướng Nhiệt Độ
# Xác định ngày có nhiệt độ cao nhất và thấp nhất
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
day_max_temp = np.argmax(temperatures) + 1  # Thêm 1 vì index bắt đầu từ 0
day_min_temp = np.argmin(temperatures) + 1
print(f"Nhiệt độ cao nhất là {max_temp}°C vào ngày {day_max_temp}")
print(f"Nhiệt độ thấp nhất là {min_temp}°C vào ngày {day_min_temp}")

# Thống kê sự chênh lệch nhiệt độ giữa các ngày
temp_diff = np.diff(temperatures)
max_diff_day = np.argmax(np.abs(temp_diff)) + 1  # Ngày có biến đổi nhiệt lớn nhất
print(f"Ngày có sự biến đổi nhiệt độ lớn nhất là ngày {max_diff_day}")

# 3. Áp Dụng Fancy Indexing
# Lọc ra ngày có nhiệt độ cao hơn 20°C
days_above_20 = np.where(temperatures > 20)[0] + 1
print("Những ngày có nhiệt độ cao hơn 20°C là:", days_above_20)

# Lấy nhiệt độ của các ngày 5, 10, 15, 20, 25
selected_days = [5, 10, 15, 20, 25]
temps_selected_days = temperatures[np.array(selected_days) - 1]
print("Nhiệt độ vào các ngày 5, 10, 15, 20, 25 là:", temps_selected_days)

# Lọc các ngày có nhiệt độ trên trung bình
above_average_days = np.where(temperatures > average_temp)[0] + 1
print("Những ngày có nhiệt độ trên trung bình là:", above_average_days)

# Lấy nhiệt độ các ngày chẵn và lẻ trong tháng
even_days_temp = temperatures[1::2]  # Ngày chẵn
odd_days_temp = temperatures[0::2]   # Ngày lẻ
print("Nhiệt độ các ngày chẵn:", even_days_temp)
print("Nhiệt độ các ngày lẻ:", odd_days_temp)
