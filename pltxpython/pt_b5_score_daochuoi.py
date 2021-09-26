# Sorting - Sắp xếp điểm thi
# Điểm thi học kỳ của sinh viên được lưu ở định dạng 1 tuple có 3 phần tử (m1, m2, e) gồm:
# m1 = midterm1
# m2 = midterm2
# e = endterm
# Cho một list gồm danh sách điểm thi của sinh viên 1 lớp. 
# Viết chương trình Python để sắp xếp danh sách trước theo thứ tự tăng dần theo phần tử cuối cùng trong mỗi tuple 
# (sắp xếp theo điểm cuối kỳ - endterm tăng dần).
# vd sort_list_last([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]) == [(10, 2, 1), (9, 1, 2), (3, 2, 3), (6, 4, 4), (1, 2, 5)]
print("Bài 1: Sắp xếp điểm thi")
score_list = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]

score_list_sorted = sorted(score_list, key = lambda x : x[2])
print(score_list, "==", score_list_sorted)

# --------------------------------------------------------------------------
# Xử lý chuỗi - Đảo ngược từ và kiểu hoa thường
# Cho 1 chuỗi A (vd: "tHE fOX iS cOMING fOR tHE cHICKEN"). 
# Viết hàm đảo ngược thứ tự các từ trong chuỗi và đổi tất cả các chữ cái từ hoa thành thường và ngược lại. 
# (kết quả là "Chicken The For Coming Is Fox The")
print("\nBài 2: Xử lý chuỗi - Đảo ngược từ và kiểu hoa thường")

A = "tHE fOX iS cOMING fOR tHE cHICKEN"

def string_revert(A):
    B = A.swapcase()
    C = B.split()[::-1]
    D = " ".join(C)
    print(A, "==", D)
    return C
string_revert(A)