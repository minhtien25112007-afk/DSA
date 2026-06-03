def dem_xuat_hien(a, x):
    """
    Hàm đếm số lần giá trị x xuất hiện trong mảng a.
    """
    # Khởi tạo biến đếm bằng 0
    count = 0
    
    # Duyệt qua từng phần tử trong mảng a
    for phan_tu in a:
        # Nếu phần tử bằng x thì tăng biến đếm lên 1
        if phan_tu == x:
            count += 1
            
    # Trả về tổng số lần xuất hiện sau khi đã duyệt hết mảng
    return count

# ==================== CHƯƠNG TRÌNH CHẠY THỬ ====================

# Dữ liệu theo ví dụ của bạn
a = [2, 5, 2, 7, 2]
x = 2

ket_qua = dem_xuat_hien(a, x)
print(f"Mảng a = {a}")
print(f"Số lần {x} xuất hiện trong mảng là: {ket_qua}")  # Kết quả sẽ in ra: 3