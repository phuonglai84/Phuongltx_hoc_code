s = "Hello World! 123"
def count_char_type(s):
    ASCII_upper = "".join(chr(x) for x in range(67, 91))
    ASCII_lower = "".join(chr(x) for x in range(97, 123))
    ASCII_num = "".join(chr(x) for x in range(48, 57))
    letter =0
    case_upper = 0
    digit = 0
    case_lower=0
    for i in range (0,len(s)):
        if s[i] in ASCII_lower or s[i] in ASCII_upper:
            letter +=1
        elif s[i] in ASCII_num:
            digit +=1 
    for j in range(0,len(s)):
        if s[j] in ASCII_lower:
            case_lower+=1
        elif s[j] in ASCII_upper:
            case_upper+=1
    print(letter, digit,case_upper,case_lower)
count_char_type(s)            



