def get_valid_int(Prompt):
    while True:
        try:
            value = int(input(Prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return value

def get_pos_int(Prompt):
    while True:
        try:
            value = int(input(Prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

# Hãy viết chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng. Vd: n = 4:
#       *
#     * *
#   * * *
# * * * *
# n = 9
# star_str = " *"
# space_str = "  "
# end_str = "\n"
# print("\n ----- Hình star 3 -----")
# for num in range(n):
#     space_number  = n - num + 1
#     star_number= num + 1
#     if star_number <= 2 or star_number == n:
#         star_text = star_number * star_str
#     else:
#         star_text = star_str +  space_str * (star_number - 2) + star_str
#     if star_number == n:
#         end_str =""
#     print(star_text.rstrip() , end = end_str)


# for num in range(n):
#     star_number = n - num
#     space_number  = n  + num
#     if num == 0: space_number = 0
#     if star_number <= 2 or star_number == n:
#         star_text = star_number * star_str
#     else:
#         star_text = star_str +  space_str * (star_number - 2) + star_str
print("\nBài tập Python buổi 3")
print("Bài 1----------------------Tạo 3 pattern tam giác sao")
n = get_pos_int("Nhập số số sao 1 cạnh tam giác, n = ")

print("1.1 Tam giác vuông phải:")
for i in range(0, n+1):
    for j in range(0, n-i):
        print("", end="  ")

    for j in range(n-i, n):
        print(" *", end="")

    print()

print("\n 1.2 2 tam giác đặc ngược:")
for i in range(0, 2*n+1):
    if i < n:
        for j in range(0, n-i):
            print("", end="  ")
        for j in range(n-i, n):
            print(" *", end="")
    elif i == n:
        for j in range(0, 2*n):
            print(" *", end="")
    else:
        for j in range(0, n):
            print("", end="  ")
        for j in range(n, 2*n-i+n):
            print(" *", end="")
    print()

print("1.3 2 tam giác rỗng ngược:\n")

for i in range(1, 2*n):
    if i < n:
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    elif i == n:
        for j in range(1, 2*n+1):
            print("*", end=" ")
    else:
        for j in range(1, 2*n + 1):
            if j == 2*n or j == i+1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

print("\nBài 2--Tạo dict với key trong list + value là count số lần lặp key--------------------")
# Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
# my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
# Trả ra
# {10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}

my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2,
    2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
my_dict = {}
print("my_list = ", my_list)

my_dict[my_list[0]] = 1
for i in range(1, len(my_list)-1):
    if my_list[i] == my_list[i-1]:
        my_dict[my_list[i-1]] += 1
    else:
        my_dict[my_list[i]] = 1
print("convert to dict = ", my_dict)

print("\nBài 3--Count tới xmas 2021 5 lần, mỗi lần cách 5s--------------------")
# Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.
# vd in ra sau mỗi 5s:
# Countdown to Xmas 2021: 112 days, 11:47:01.339588
# Countdown to Xmas 2021: 112 days, 11:46:56.324008
# Countdown to Xmas 2021: 112 days, 11:46:51.310473
from datetime import date, time, datetime, timedelta
import time 

n = 5  # in ra kq 5 lần sau mỗi 5s
t0 = datetime.now().replace(microsecond=0)
tx = t0 + timedelta(seconds=5*n)
t2 = datetime(2021, 12, 25, 00, 00, 00)

while datetime.now() < tx:
    t1 = datetime.now().replace(microsecond=0)
    print("Countdown to Xmas 2021: ", t2 - t1)
    time.sleep(5)

print("\nBài 4--Tìm set value duy nhất của list dict--------------------")
# Unique value Dictionary:
# Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.
# [VD1]: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất.
# unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}
# [VD2]: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.
# unique_value_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S009', 'S007', 'S002', 'S001', 'S005'}

list1 = [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
list2 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
    "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
list3 = list1 + list2
print("in list all = ", list3, "\n")

new_set = set()
for i in range(0, len(list3)):
    list_value_i = list(list3[i].values())
    # print(i, list_value_i, end=(" "))
    new_set.update(list_value_i)
    # print(new_set)

print("\nFinal result Set value duy nhất = ", new_set)

print("\nBài 5--Tìm cặp số trong list A có tổng = num--------------------")
# Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
# Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
# vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []

print("Nhập số nguyên để tạo list, số bất kỳ để stop:")
list_A = []
while True:
    try:
        value = int(input())
    except ValueError:
        break
    else:
        list_A.append(value)

set_A = set(list_A)
list_A_unique = list(set_A)
print("List số nguyên tăng dần = ", list_A_unique)

sum = get_valid_int("Tìm cặp số có tổng = ")

list_capso = []
for i in range(0, len(list_A_unique)):
    count_capso = 0
    for j in range(i+1, len(list_A_unique)):
        if list_A_unique[i] + list_A_unique[j] == sum:
            count_capso +=1
            if count_capso == 1:
                list_capso.extend([(list_A_unique[i], list_A_unique[j])])
print(list_capso)




