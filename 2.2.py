# Insertion Sort

def insertion_sort(arr):
    n = len(arr)

    # Nếu mảng có 0 hoặc 1 phần tử thì đã được sắp xếp
    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]      # Phần tử cần chèn
        j = i - 1

        # Di chuyển các phần tử lớn hơn key sang phải
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


arr = [12, 11, 13, 58, 6, 90, 55]

insertion_sort(arr)

print(arr)