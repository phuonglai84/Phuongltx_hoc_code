# Regex - ApacheLog

# Logfile của webserver apache gồm nhiều dòng với mỗi dòng có định dạng như sau

# 10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET xxxxxx HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"

# Trong đó xxxxxx có thể là đường dẫn đến một thư mục hoặc file bất kỳ của server.
# Dùng regex để lọc lấy ra tất cả các đường dẫn đến file .jpg trong các file log đầu vào dưới đây.
# Loại bỏ các đường dẫn trùng nhau và trả ra danh sách các đường dẫn.
# Định dạng của mỗi đường dẫn trả ra trong list nên là:
# "http://host/path" với

# host là phần cuối của tên logfile
# path là phần xxxxxx được trích xuất phía trên
