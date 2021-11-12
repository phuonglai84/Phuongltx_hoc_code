import re
from prettytable import PrettyTable

filename = "baby1990.html"
def extract_names(filename):
    """
    Cho một file .html, trả ra list bắt đầu bằng năm, 
    theo sau bởi các chuỗi tên-xếp hạng theo thứ tự abc.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    file_open = open("D:\\Learning\\Python\\Phuongltx_hoc_code\\pltxpython\\hackathon1_midterm/" + filename, encoding='utf-8-sig')
    # test = """<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
    #  <tr align="right"><td>2</td><td>a</td><td>He</td>"""
    row_list = re.findall("<td>([a-zA-Z1-9]+)", file_open.read(), re.MULTILINE)

    name_list = re.findall("\d{4}", filename)
    for i in range(0, len(row_list), 3):
        name_list.append(f"{row_list[i+1]} {row_list[i]}")
        name_list.append(f"{row_list[i+2]} {row_list[i]}")
    
    name_list.sort()

    x = PrettyTable(["No.", name_list[0]])
    result = open("D:/Learning/Python/Phuongltx_hoc_code/pltxpython/hackathon1_midterm/result.txt", 'w')
    result.write(f"No.\t\t{name_list[0]}\n")

    for i in range(10):          #(len(name_list)-1):
        x.add_row([i+1, name_list[i+1]])
        y = f"{i+1}\t\t{name_list[i+1]}\n"
        result.write(y)

    print(x)

    return name_list


goiham = extract_names(filename)
