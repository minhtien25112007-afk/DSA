a = [3, 2, 1]

shift = 0

for i in range(1, len(a)):

    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        shift += 1
        j -= 1

    a[j + 1] = key

print("Mang:", a)
print("So shift:", shift)