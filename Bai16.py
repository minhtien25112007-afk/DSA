# Hàm tìm phần tử gần x nhất
def tim_gan_x_nhat(arr, x):
    gan_nhat = arr[0]
    vi_tri = 0
    chenhlech_min = abs(arr[0] - x)

    for i in range(1, len(arr)):
        chenhlech = abs(arr[i] - x)

        if chenhlech < chenhlech_min:
            chenhlech_min = chenhlech
            gan_nhat = arr[i]
            vi_tri = i

    return gan_nhat, vi_tri


# Mảng ví dụ
arr = [3, 8, 15, 20, 27]
x = 18

# Gọi hàm
gia_tri, vi_tri = tim_gan_x_nhat(arr, x)

# In kết quả
print("Phần tử gần", x, "nhất là:", gia_tri)
print("Vị trí:", vi_tri)
