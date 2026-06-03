def tim_min_max_dong_thoi(a):
    """
    Hàm tìm đồng thời giá trị lớn nhất, nhỏ nhất và vị trí của chúng trong 1 lần duyệt.
    """
    # Kiểm tra mảng rỗng
    if len(a) == 0:
        print("Mảng rỗng!")
        return

    # Bước 1: Khởi tạo giá trị ban đầu tại phần tử đầu tiên
    max_val = min_val = a[0]
    max_idx = min_idx = 0

    # Bước 2: Duyệt tuyến tính đúng 1 lần từ phần tử thứ 2
    for i in range(1, len(a)):
        # Kiểm tra để cập nhật Max
        if a[i] > max_val:
            max_val = a[i]
            max_idx = i
        
        # Kiểm tra để cập nhật Min (Sử dụng if độc lập để xét cả hai trường hợp)
        if a[i] < min_val:
            min_val = a[i]
            min_idx = i

    # Bước 3: In kết quả ra màn hình
    print(f"Mảng dữ liệu: {a}")
    print("-" * 40)
    print(f"-> Giá trị lớn nhất là: {max_val} (tại chỉ số/index: {max_idx})")
    print(f"-> Giá trị nhỏ nhất là: {min_val} (tại chỉ số/index: {min_idx})")

# ==================== CHƯƠNG TRÌNH CHẠY THỬ ====================

# Sử dụng mảng mẫu
mang_a = [7, 3, 9, 12, 5, 8, 1]

tim_min_max_dong_thoi(mang_a)