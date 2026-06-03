def sort_students(students):
    n = len(students)

    # Sắp xếp tên tăng dần
    for i in range(n):
        for j in range(n - i - 1):
            if students[j][0] > students[j + 1][0]:
                students[j], students[j + 1] = students[j + 1], students[j]

    # Sắp xếp điểm giảm dần
    for i in range(n):
        for j in range(n - i - 1):
            if students[j][1] < students[j + 1][1]:
                students[j], students[j + 1] = students[j + 1], students[j]

    print(students)

a = [('An',8), ('Ba',9), ('Cu',8)]
sort_students(a)