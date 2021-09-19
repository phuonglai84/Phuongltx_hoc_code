# 1
# Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. 
# Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). 
# Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05
def day_diff(release_date, code_complete_day):
    from datetime import date
    from datetime import time
    from datetime import datetime
    
    d1 = datetime.strptime(release_date, "%d/%m/%Y")
    d2 = datetime.strptime(code_complete_day, "%Y-%d-%m")
    d = (d1-d2).days
    print("Days to test = ", d, "days")
    return d

# 2
# Viết hàm alpha_num() tìm tất cả những từ trong một câu có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
# Vd:
# str1 = "Emma25 is Data scientist50 and AI Expert"
# alpha_num(str1) == ["Emma25", "scientist50"]
def alpha_num(sentence):
    # c1 làm bài này    
    # result = []
    # values = sentence.split()
    # print(values)
    # for i in values:
    #     check = i.isalnum() and not i.isalpha() and not i.isdigit()
    #     if check:
    #         result.append(i)
    # print(result)
    # c2 làm bài này
    import re
    matched = re.findall(r'(?:[a-zA-Z]+\d+|\d+[a-zA-Z]+)[a-zA-Z\d]*(?=\s|$)', sentence)
    print(matched)
    return matched
    # return result

# day_diff("19/12/2021", "2021-17-09")
alpha_num("Emma25 is Data scientist50 and AI Expert 84pltx 45xxx67 ab3de5f")
