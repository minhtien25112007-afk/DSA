a = [1, 2, 3]
n = len(a)

swap = 0

for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    if min_index != i:
        a[i], a[min_index] = a[min_index], a[i]
        swap += 1

print("Mang:", a)
print("So swap:", swap)