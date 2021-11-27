s= str(input("Nhập chuỗi: ")) 
def reserve_string(s):
    split_str = s.split()
    join_str = ' '.join(split_str[::-1])
    print(join_str.swapcase())
reserve_string(s)