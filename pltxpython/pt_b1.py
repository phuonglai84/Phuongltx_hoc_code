#Nhập nhiệt độ (°C - float)
#Quy đổi và in ra °F tương ứng (°F = °C * 9 / 5 + 32)
#Quy đổi và in ra °K tương ứng (°K = °C + 273.15)
#Quy đổi và in ra °R tương ứng (°R = (°C + 273.15) * 9 / 5))

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        temp_c = float(input("Nhiệt độ hôm nay theo độ C: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #value was successfully parsed!
        #we're ready to exit the loop.
        break
temp_f = temp_c * 9 / 5 + 32
temp_k = temp_c + 273.15
temp_r = (temp_c + 273.15) * 9 / 5
print("~ " + str(temp_f) + " độ F")
print("~ " + str(temp_k) + " độ K")
print("~ " + str(temp_r) + " độ R")

#-----------------------
# Viết chương trình quy đổi độ dài từ đơn vị km sang các đơn vị khác

# Nhập giá trị độ dài length - float (đơn vị km)
# Quy đổi sang các đơn vị m, dm, cm, mm, mile, inch và in kết quả (làm tròn đến 2 chữ số thập phân)
# 💡 Bảng đơn vị

# 1 km = 1000 m
# 1 km = 10000 dm
# 1 km = 100000 cm
# 1 km = 1000000 mm
# 1 km = 1.609344 mile
# 1 km = 39370.1 inch
# Có thể thêm một số đơn vị khác

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        length = float(input("Số km bạn muốn đổi: "))
    except ValueError:
        print("K phải dạng số.")
        #better try again... Return to the start of the loop
        continue
    else:
        #value was successfully parsed!
        #we're ready to exit the loop.
        break

while True:
    length_unit = input("Pick length unit you want to convert to (mm/cm/dm/m/mile/inch): ")
    if length_unit.lower() not in ('mm', 'cm', 'dm', 'm', 'mile', 'inch'):
        print("Chỉ nhập trong: mm/cm/dm/m/mile/inch")
    else:
        break

if length_unit.lower() == 'mm':
    print('1km = '+ str(round(length * 1000000, 2)) + ' mm')
elif length_unit.lower() == 'cm':
    print('1km = '+ str(round(length * 100000, 2)) + ' cm')
elif length_unit.lower() == 'dm':
    print('1km = '+ str(round(length * 10000, 2)) + ' dm')
elif length_unit.lower() == 'm':
    print('1km = '+ str(round(length * 1000, 2)) + ' m')       
elif length_unit.lower() == 'mile':
    print('1km = '+ str(round(length * 1.609344, 2)) + ' mile')  
elif length_unit.lower() == 'inch':
    print('1km = '+ str(round(length * 39370.1, 2)) + ' inch')           

print('-----------------------')
#-------------------------------------------
# Viết chương trình chuyển đổi từ số giây (nguyên dương) thành giờ, phút, giây tương ứng

# Nhập số giây sec (int)
# Quy đổi và in ra giá trị giờ phút giây tương ứng
# 💡 VD: Nhập 123 -> 0 giờ, 2 phút, 3 giây

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        time_ss = int(input("Số second bạn muốn đổi: "))
    except ValueError:
        print("Số second không hợp lệ.")
        #better try again... Return to the start of the loop
        continue
    else:
        #value was successfully parsed!
        #we're ready to exit the loop.
        if time_ss < 0:
            print('Số second không được âm.')
        else:
            break

time_hh = time_ss//3600
time_mm = time_ss%3600//60

print('chuẩn second rồi, ~ '+ str(time_hh) + ' giờ ' + str(time_mm) + ' phút ' + str(time_ss%3600%60) + ' giây')