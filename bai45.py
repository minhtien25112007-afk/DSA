
a = [8,7,6,5,4,3,2,1]

gap = len(a)//2

while gap > 0:

    for i in range(gap, len(a)):

        temp = a[i]
        j = i

        while j >= gap and a[j-gap] > temp:
            a[j] = a[j-gap]
            j -= gap

        a[j] = temp

    gap //= 2

print(a)