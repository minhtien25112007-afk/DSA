a = [5, 2, 4, 6, 1]
n = len(a)

compare = 0

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        compare += 1

        if a[j] < a[min_index]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print("Mang:", a)
print("So lan so sanh:", compare)