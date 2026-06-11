def tim_min(a, i):
    min_index = i

    for j in range(i + 1, len(a)):
        if a[j] < a[min_index]:
            min_index = j

    return min_index


a = [9, 3, 7, 1, 5]

print(tim_min(a, 1))