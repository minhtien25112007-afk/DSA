# Selection Sort cho mảng chuỗi

arr = ["banana", "apple", "orange", "grape", "mango"]

n = len(arr)

for i in range(n):
    min_index = i

    # Tìm chuỗi nhỏ nhất theo thứ tự từ điển
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Hoán đổi vị trí
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Mảng sau khi sắp xếp là:")
print(arr)