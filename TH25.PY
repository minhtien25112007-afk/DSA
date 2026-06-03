def bubble_sort_invariant(arr):
    a = arr[:]
    n = len(a)

    for i in range(n - 1):

        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

        print("Sau lượt", i + 1, ":", a)
        print("Phần cuối đã đúng vị trí:",
              a[n - i - 1:])

a = [5, 1, 4, 2, 8]
bubble_sort_invariant(a)