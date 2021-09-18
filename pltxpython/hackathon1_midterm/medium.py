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
def roman_to_int(s):
    pass


roman_to_int("LVIII")
roman_to_int("IX")
roman_to_int("MCMXCIV")




