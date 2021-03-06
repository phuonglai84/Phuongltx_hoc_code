#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Python for Tester - OneMount Class
# Quang Le - quangdle@gmail.com - 09/2021

#https://quantrimang.com/lam-viec-voi-file-trong-python-160073

import sys
import re
from prettytable import PrettyTable

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

def main():
  # Chương trình này có thể nhận đối số đầu vào là một hoặc nhiều tên file
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # Với mỗi tên file, gọi hàm extract_names ở trên và in kết quả ra stdout
  # hoặc viết kết quả ra file summary (nếu có input --summaryfile).
  
if __name__ == '__main__':
  main()
