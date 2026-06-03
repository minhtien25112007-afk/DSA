def linear_search(A, x):
    """
    Hàm tìm kiếm tuyến tính.
    Trả về chỉ số (index) của x trong mảng A nếu tìm thấy.
    Trả về -1 nếu không tìm thấy.
    """
    # Duyệt qua từng chỉ số i từ 0 đến hết chiều dài của mảng
    for i in range(len(A)):
        # So sánh giá trị tại vị trí i với x
        if A[i] == x:
            return i  # Trường hợp 1: Tìm thấy thành công, trả về chỉ số i và dừng hàm
            
    return -1  # Trường hợp 2: Đã duyệt hết danh sách mà không thấy, trả về -1

# --- Chạy thử nghiệm với dữ liệu từ ví dụ trước ---
A = [7, 3, 9, 12, 5, 8, 1]
x = 5

ket_qua = linear_search(A, x)

# In kết quả ra màn hình
if ket_qua != -1:
    print(f"Tìm thấy {x} tại chỉ số (index): {ket_qua}")
else:
    print(f"Không tìm thấy {x} trong mảng.")