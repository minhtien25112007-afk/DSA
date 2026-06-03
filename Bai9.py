def tim_tat_ca(a, x):
    """
    Hàm tìm tất cả các vị trí (chỉ số) xuất hiện của x trong mảng a.
    Trả về một danh sách chứa các chỉ số đó.
    """
    # Khởi tạo một danh sách rỗng để chứa các vị trí tìm thấy
    danh_sach_chi_so = []
    
    # Duyệt qua từng chỉ số i từ 0 đến len(a) - 1
    for i in range(len(a)):
        # Nếu phần tử tại vị trí i bằng x
        if a[i] == x:
            # Thêm chỉ số i vào danh sách kết quả
            danh_sach_chi_so.append(i)
            
    # Trả về danh sách các chỉ số thu được
    return danh_sach_chi_so

# ==================== CHƯƠNG TRÌNH CHẠY THỬ ====================

# Trường hợp 1: Phần tử x xuất hiện nhiều lần (theo ví dụ của bạn)
a1 = [4, 1, 4, 9, 4]
x1 = 4
print(f"Mảng: {a1}, x = {x1} -> Vị trí: {tim_tat_ca(a1, x1)}") 
# Kết quả: [0, 2, 4]

# Trường hợp 2: Phần tử x không có trong mảng
a2 = [4, 1, 4, 9, 4]
x2 = 7
print(f"Mảng: {a2}, x = {x2} -> Vị trí: {tim_tat_ca(a2, x2)}") 
# Kết quả: [] (Danh sách rỗng)