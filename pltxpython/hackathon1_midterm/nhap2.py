import sys
import re
import io

"""Baby Names exercise

Định nghĩa hàm extract_names() dưới đây và gọi từ hàm main().

Cấu trúc các tag html trong các file baby.html như sau:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Các bước nên làm tuần tự:
 -Trích xuất năm
 -Lấy và in ra tên và thứ hạng phổ biến
 -Xây danh sách [year, 'name rank', ... ] và in ra
 -Sửa hàm main() để dùng hàm extract_names.
"""

def extract_names(filename):
  """
  Cho một file .html, trả ra list bắt đầu bằng năm, 
  theo sau bởi các chuỗi tên-xếp hạng theo thứ tự abc.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  year = 0
  list_data = []
  with open(filename, "r", encoding='utf-8-sig') as file:
    for line in file:
      if(year == 0):
        re_year = re.search("Popularity in (\d+)", line)
        if(re_year): 
          year = re_year.groups()[0]
          
      re_name = re.findall("<td>(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>", line)  
      if(re_name):
        list_data.append(re_name[0][1] + " " + re_name[0][0])
        list_data.append(re_name[0][2] + " " + re_name[0][0])
  list_data.sort(); 
  list_data.insert(0, year)     
  return list_data  

filename = "baby1990.html"
x = extract_names(filename)
print(x)