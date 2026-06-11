a = [7,2,5,1,9]
k = 3
for i in range(k):

    min_idx = i

    for j in range(i+1,len(a)):
        if a[j] < a[min_idx]:
            min_idx = j

    a[i],a[min_idx] = a[min_idx],a[i]

print(a[k-1])