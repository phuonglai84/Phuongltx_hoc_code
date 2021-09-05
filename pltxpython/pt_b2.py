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
# ---------------------------------
# Viết chương trình Python kiểm tra số lớn nhất trong 3 số
# Khai báo 3 biến a, b, c nhập giá trị số bất kỳ (int)
# Kiểm tra và in ra số lớn nhất trong 3 số đó

no1 = get_valid_int("Please enter no1: ")
no2 = get_valid_int("Please enter no2: ")
no3 = get_valid_int("Please enter no3: ")

no_list = [no1, no2, no3]
print("Max of " + str(no_list) + " = " + str(max(no1, no2, no3)) )

print("---------------------------------------")
# Viết chương trình kiểm tra một năm có phải năm nhuận hay không
# Nhập một năm year - int
# Kiểm tra và in ra kết quả year có phải năm nhuận hay không
# 💡 Năm nhuận là năm:
# Chia hết cho 400
# Chia hết cho 4 nhưng không chia hết cho 100

year = get_valid_int("Nhập số năm muốn check nhuận hay k: ")

if year%400 == 0 or (year%4 == 0 and year%100 != 100):
    print("Năm nhuận đấy!!!")
else:
    print("Không phải năm nhuận.")    

print("---------------------------------------")
# Viết chương trình tính chỉ số BMI (Body Mass Index - Chỉ số cơ thể)
# Nhập chiều cao h (đơn vị m) và cân nặng w (đơn vị kg)
# Tính chỉ số BMI: w / (h * h)
# In chỉ số và thông báo kết quả theo quy ước:
# BMI < 17: Gầy độ II
# 17 <= BMI < 18.5: Gầy độ I
# 18.5 <= BMI < 25: Bình thường
# 25 <= BMI < 30: Thừa cân
# 30 <= BMI < 35: Béo phì độ I
# 35 <= BMI: Béo phì độ II

def get_pos_float(Prompt):
    while True:
        try:
            value = float(input(Prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

h = get_pos_float("Your height in m: ")
w = get_pos_float("Your weight in kg: ")

BMI = round(w/(h*h), 1)
print("Your BMI = " + str(BMI))

if BMI < 17:
    print("BMI < 17: Gầy độ II")
elif BMI >= 17 and BMI < 18.5:
    print("17 <= BMI < 18.5: Gầy độ I")
elif BMI >= 18.5 and BMI < 25:
    print("18.5 <= BMI < 25: Bình thường")
elif BMI >= 25 and BMI < 30:
    print("25 <= BMI < 30: Thừa cân")
elif BMI >= 30 and BMI < 35:
    print("30 <= BMI < 35: Béo phì độ I")    
else:     
    print("35 <= BMI: Béo phì độ II")    
 
