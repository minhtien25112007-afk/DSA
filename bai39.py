a = [('An',8), ('Ba',9), ('Cu',8)]

for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and (
        a[j][1] < key[1] or
        (a[j][1] == key[1] and a[j][0] > key[0])
    ):
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key

print(a)