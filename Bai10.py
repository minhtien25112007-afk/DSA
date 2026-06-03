def tim_vi_tri_cuoi_cung_cach1(a, x):
    """
    Duyệt ngược từ cuối mảng về đầu mảng.
    """
    n = len(a)
    # range(start, stop, step) -> chạy từ n-1 về 0, mỗi bước giảm 1 đơn vị
    for i in range(n - 1, -1, -1):
        if a[i] == x:
            return i  # Gặp phát đầu tiên khi đi lùi -> chính là vị trí cuối cùng
            
    return -1  # Duyệt hết mà không thấy

def tim_vi_tri_cuoi_cung_cach2(a, x):
    """
    Duyệt xuôi từ đầu đến cuối mảng và cập nhật vị trí mới nhất.
    """
    vi_tri_cuoi = -1  # Khởi tạo ban đầu là -1 (coi như chưa thấy)
    
    for i in range(len(a)):
        if a[i] == x:
            vi_tri_cuoi = i  # Cập nhật liên tục, giữ lại vị trí sau cùng
            
    return vi_tri_cuoi

# Mảng kiểm thử: số 4 xuất hiện ở các chỉ số 0, 2, và 5
mang_a = [4, 1, 4, 9, 7, 4, 2]
x_can_tim = 4

kq1 = tim_vi_tri_cuoi_cung_cach1(mang_a, x_can_tim)
kq2 = tim_vi_tri_cuoi_cung_cach2(mang_a, x_can_tim)

print(f"Mảng: {mang_a}")
print(f"Vị trí cuối cùng của {x_can_tim} (Cách 1 - Duyệt ngược): {kq1}")  # Kết quả: 5
print(f"Vị trí cuối cùng của {x_can_tim} (Cách 2 - Duyệt xuôi) : {kq2}")  # Kết quả: 5

# Thử nghiệm với số không có trong mảng
print(f"Vị trí cuối cùng của số 100: {tim_vi_tri_cuoi_cung_cach1(mang_a, 100)}")  # Kết quả: -1