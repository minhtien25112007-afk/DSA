a = ['abc', 'a', 'ab']

for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and len(a[j]) > len(key):
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key

print(a)