def min_passes(arr):
    sorted_arr = sorted(arr)

    pos = {}
    for i, x in enumerate(sorted_arr):
        if x not in pos:
            pos[x] = []
        pos[x].append(i)

    used = {}
    answer = 0

    for i, x in enumerate(arr):
        if x not in used:
            used[x] = 0

        target = pos[x][used[x]]
        used[x] += 1

        answer = max(answer, i - target)

    return answer

a = [1, 2, 3, 5, 4]
print(min_passes(a))