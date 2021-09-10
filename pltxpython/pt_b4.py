# Function - Đếm loại ký tự
# Viết hàm có đầu vào là 1 chuỗi, trả ra số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi đó. Giả sử đầu vào sau được cấp cho hàm:
# s = "Hello World! 123"
# Hàm count_char_type(s) sẽ trả ra 1 dict {"LETTERS":10, "CASE": {"UPPER CASE":2, "LOWER CASE":8}, "DIGITS":3}. Lưu ý: value của key "CASE" là một dict có 2 keys là "UPPER CASE", "LOWER CASE".
# a) Viết hàm trên dùng bất kỳ hàm built in nào của python
# b) Viết hàm chỉ dùng 1 hàm built in duy nhất.
from statistics import mean, median, mode
from typing import Counter


print("-----------------------------------------------------")
print("Buổi 4 - Bài 1, count string Upper/Lower/Degit")

def count_char_type(s):
    count1, count2, count3 = 0, 0, 0
    for i in s:
        if i.isupper():
            count1 += 1
        if i.islower():
            count2 += 1
        if i.isdigit():
            count3 += 1    
    print("Count character kiểu a nhiều buildin: ", {'UPPER CASE': count1, 'LOWER CASE': count2, 'DIGIT': count3})

def count_char_type2(s):
    count1, count2, count3 = 0, 0, 0
    for i in s:
        ord(i)
        if 65 <= ord(i) <= 90:
            count1 += 1
        if 97 <= ord(i) <= 122:
            count2 += 1
        if 48 <= ord(i) <= 57:
            count3 += 1
    print("Count character kiểu b 1 buildin ord: ", {'UPPER CASE': count1, 'LOWER CASE': count2, 'DIGIT': count3})

s = "Hello World! 123"
print("Chuỗi gốc: ", s)
count_char_type(s)
count_char_type2(s)


# Function - Chỉ số thống kê mô tả
# Cho một list A các điểm thi (từ 0-10) của các học viên trong lớp. Viết 3 hàm tính:
# giá trị trung bình (mean) của dãy.
# trung vị (median) của dãy A. trung vị là một số đứng ở vị trí giữa trong dãy số đã được sắp xếp theo thứ tự tăng dần, median chia dãy số cho trước thành 2 nửa bằng nhau. Nếu độ dài của dãy số là số lẻ, thì số ở giữa là median, nếu chiều dài của dãy số là số chẵn thì median được xác định bằng cách lấy trung bình của hai số ở giữa.
# mode của dãy A. Mode là phần tử có số lần xuất hiện nhiều nhất trong dãy. Mode sẽ giúp ta trả lời câu hỏi: "Trong lớp này, học viên đạt Điểm số nào nhiều nhất?".
# Lưu ý: kết quả trả ra sẽ là 1 list vì mode có thể nhiều hơn 1 giá trị.
# Vd:
# A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10] ==> (mean(A), median(A), mode(A)) == (6.55, 7.0, [9])
# B=[4,4,5,4,5,5] thì (mean(B), median(B), mode(B)) == (4.5, 4.5, [4,5])
print("-----------------------------------------------------")
print("Buổi 4 - Bài 2, tính mean, median, mode của list")

A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
# A = [4,4,5,4,5,5]

def cal_mean(a):
    import random
    import statistics

    mean_list = statistics.mean(a)
    return mean_list

def cal_median(a):
    import random
    import statistics
    
    median_list = statistics.median(a)
    return median_list    

def cal_mode(a):
    m_count = 0
    m_set = set()
    mode_list = []
    for i in A:
        A.count(i)
        if A.count(i) > m_count:
            m_count = A.count(i)     
    for i in A:
        A.count(i)
        if A.count(i) == m_count:
            m_set.add(i)
    mode_list = list(m_set)
    return mode_list

print("A = ", A, "==> (mean(A), median(A), mode(A)) == ", [cal_mean(A), cal_median(A), cal_mode(A)])