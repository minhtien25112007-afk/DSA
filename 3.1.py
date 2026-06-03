# Selection Sort

arr = [140, 25, 15, 52, 10, 250, 55]

for i in range(len(arr)):

    # Tìm phần tử nhỏ nhất trong đoạn chưa sắp xếp
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    # Đổi chỗ phần tử nhỏ nhất với vị trí hiện tại
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array")

for i in range(len(arr)):
    print("%d" % arr[i])