def cocktail_shaker_sort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # trái → phải
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # phải → trái
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

    print(arr)

a = [5, 1, 4, 2, 8]
cocktail_shaker_sort(a)