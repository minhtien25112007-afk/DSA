def linear_search(a, x):
    """
    Hàm tìm kiếm tuyến tính.
    Trả về vị trí (chỉ số) đầu tiên của x trong mảng a.
    Trả về -1 nếu x không tồn tại trong mảng.
    """
    for i in range(len(a)):
        if a[i] == x:
            return i  # Trả về vị trí đầu tiên tìm thấy và dừng hàm
    return -1  # Duyệt hết mảng mà không thấy x


# ==================== CHƯƠNG TRÌNH CHÍNH ====================

# 1. Nhập mảng từ bàn phím
# Người dùng nhập các số cách nhau bằng dấu cách, ví dụ: 7 3 9 12 5 8 1
input_string = input("Nhập các phần tử của mảng (cách nhau bởi dấu cách): ")

# Chuyển chuỗi vừa nhập thành một danh sách các số nguyên
a = [int(item) for item in input_string.split()]

# 2. Nhập giá trị x cần tìm
x = int(input("Nhập giá trị x cần tìm: "))

# 3. Gọi hàm tìm kiếm và lưu kết quả
vi_tri = linear_search(a, x)

# 4. In kết quả ra màn hình
print("-" * 40)
if vi_tri != -1:
    print(f"Giá trị {x} xuất hiện đầu tiên tại chỉ số (index): {vi_tri}")
else:
    print(f"Giá trị {x} không có trong mảng (Kết quả: {vi_tri})")