# Danh sách danh bạ
danh_ba = []


# Hàm thêm liên hệ
def them_lien_he():
    ten = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")

    lien_he = {
        "ten": ten,
        "sdt": sdt
    }

    danh_ba.append(lien_he)
    print("Đã thêm liên hệ")


# Hàm tìm số điện thoại theo tên
def tim_sdt_theo_ten():
    ten = input("Nhập tên cần tìm: ")

    for lh in danh_ba:
        if lh["ten"].lower() == ten.lower():
            print("Số điện thoại:", lh["sdt"])
            return

    print("Không tìm thấy liên hệ")


# Hàm tìm tên theo số điện thoại
def tim_ten_theo_sdt():
    sdt = input("Nhập số điện thoại cần tìm: ")

    for lh in danh_ba:
        if lh["sdt"] == sdt:
            print("Tên liên hệ:", lh["ten"])
            return

    print("Không tìm thấy liên hệ")


# Hàm đếm số điện thoại theo đầu số
def dem_theo_dau_so():
    dau_so = input("Nhập đầu số: ")
    dem = 0

    for lh in danh_ba:
        if lh["sdt"].startswith(dau_so):
            dem += 1

    print("Số liên hệ có đầu số", dau_so, "là:", dem)


# Menu chương trình
while True:
    print("\n===== MENU DANH BẠ =====")
    print("1. Thêm liên hệ")
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại")
    print("4. Đếm số liên hệ theo đầu số")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        them_lien_he()

    elif chon == "2":
        tim_sdt_theo_ten()

    elif chon == "3":
        tim_ten_theo_sdt()

    elif chon == "4":
        dem_theo_dau_so()

    elif chon == "0":
        print("Kết thúc chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")