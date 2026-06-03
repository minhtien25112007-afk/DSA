# Insertion Sort

def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        # Di chuyển các phần tử lớn hơn key
        # sang phải một vị trí
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


arr = [12, 31, 130, 15, 18, 150, 30]

insertion_sort(arr)

print("Mảng sau khi sắp xếp là:")
for i in range(len(arr)):
    print("%d" % arr[i])