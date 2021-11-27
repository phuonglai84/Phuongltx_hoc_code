#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Quang Le - Techmaster.vn - 09/2021


"""Wordcount exercise

Hàm main() đã được định nghĩa hoàn chỉnh ở dưới. Bạn phải viết hàm get_words()
và get_top_words() mà sẽ được gọi từ main().

1. Với đối số --count, viết hàm get_words(filename) đếm số lần xuất hiện của mỗi từ 
trong file đầu vào và trả list các tuple theo định dạng sau:
[(word1, count1), 
(word2, count2)
...]

Trả ra danh sách trên theo thứ tự từ điển các từ (python sẽ sắp xếp dấu câu đứng trước
các chữ cái nên cũng không thành vấn đề). Lưu tất cả các từ dưới dạng chữ thường,
vì vậy 'The' và 'the' được tính là cùng một từ.

2. Với đối số --topcount, viết hàm get_top_words(filename) tương tự như get_words()
nhưng chỉ trả ra 20 từ thông dụng nhất sắp xếp theo từ thông dụng nhất ở trên cùng.

Tùy chọn: định nghĩa một hàm helper để tránh lặp lại code trong các hàm 
get_words() và get_top_words().

"""
import sys
def word_count(filename):   
  dict_1 = {}
  f=open(filename,'r')
  text = ((f.read()).lower()).split() 
  for word in text:                   
    if word in dict_1.keys():
      dict_1[word] += 1
    else:
      dict_1[word] = 1
  return dict_1                       

def get_words(filename):
  dict_2 = word_count(filename)
  for k in sorted(dict_2.keys()):   
    print (k,dict_2[k])


def get_top_words(filename):
  dict_2 = word_count(filename)
  def get_value(tup):
    return tup[-1]
  dict_3 = sorted(dict_2.items(),key=get_value,reverse=True)                                                              
  for k,v in dict_3[:20]:
    print (k,v)

def main():                                  
  if len(sys.argv) != 3: 
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    get_words(filename)
  elif option == '--topcount':
    get_top_words(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()