#3
# Viết hàm anagram_number() 
# có đầu vào là một số nguyên 
# và trả ra True nếu sau khi đảo ngược thứ tự các chữ số của số đó vẫn cho ta số ban đầu. 
# Trả ra False nếu không giống.
# vd: anagram_number(121121) == True
#     anagram_number(1254) == False
def anagram_number(number):
    new_str = str(number)[::-1]
    new_no = int(new_str)
    print("anagram_number(" + str(number) + ") ==", new_no == number)
    return new_no == number

# anagram_number(12131213)
# anagram_number(12134)
# anagram_number(8888888888888)

#4
# Các chữ số La Mã được thể hiện bằng bảy biểu tượng khác nhau: I, V, X, L, C, D và M với
# I=1; V=5; X=10; L=50; C=100; D=500; M=1000

# Ví dụ: số 2 được viết là II bằng số La Mã, chỉ là hai chữ I được thêm vào với nhau. 12 được viết là XII, đơn giản là X + II. Con số 27 được viết là XXVII, là XX + V + II.

# Chữ số La mã thường được viết từ lớn nhất đến nhỏ nhất từ trái sang phải. Tuy nhiên, số 4 không viết là IIII mà được viết là IV. Bởi vì I đứng trước V, chúng ta lấy 5 - 1 = 4. Nguyên tắc tương tự cũng áp dụng cho số chín, được viết là IX. Có sáu trường hợp phép trừ được sử dụng:

# I có thể được đặt trước V (5) và X (10) để tạo thành 4 và 9.
# X có thể được đặt trước L (50) và C (100) để tạo ra 40 và 90.
# C có thể được đặt trước D (500) và M (1000) để tạo thành 400 và 900.
# Cho một chữ số la mã dạng string, hãy viết hàm roman_to_int() chuyển nó thành một số nguyên.

#c1
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
         'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
def roman_to_int(s):
    import re
    print(re.findall(r'I[XV]|X[LC]|C[DM]|[IVXLCDM]', s))
    num = sum(roman[key] for key in re.findall(r'I[XV]|X[LC]|C[DM]|[IVXLCDM]', s))
    print(s,"=",num)
    return num

# roman_to_int("LVIII")   #58
# roman_to_int("IX")      #9
# roman_to_int("MCMXCIV") #1994

#c2
# def roman_to_int(s):
#     translations = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     number = 0
#     s = s.replace("IV", "IIII").replace("IX", "VIIII")
#     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#     for char in s:
#         number += translations[char]
#     return number

#c3
# def roman_to_int(s):
#     map_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     total = 0
#     s = s.upper()
#     length = len(s)
#     for i in range(length):
#         num = map_roman.get(s[i])
#         if(i < length - 1):
#             num_next = map_roman.get(s[i+1])
#             if(num < num_next):
#                 total -= num
#             else:
#                 total += num
#         else:
#             total += num    
#     return total    