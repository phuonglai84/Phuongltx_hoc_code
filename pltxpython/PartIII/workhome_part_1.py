# Bài tập OOP buổi 1
# Thay đổi các thuộc tính account_number, account_name, balance trong class BankAccount thành thuộc tính ẩn, 
# và triển khai thêm các phương thức
# get_account_number()
# get_account_name()
# get_balance()
# set_balance() - balance phải lớn hơn hoặc bằng 0
# Thay đổi các phương thức display(), withdraw() và deposit() sử dụng các phương thức getter và setter trên.
# Chú ý:
# Với withdraw(), amount phải lớn hơn 0 và nhỏ hơn balance
# Với deposit(), amount phải lớn hơn 0
# Nếu giá trị không phù hợp thì thông báo ra console

class BankAccount:
    def __init__(self, account_number, account_name, balance = 0):          #dùng __int__() để khởi tạo
        self._account_number = account_number
        self._account_name = account_name
        self._balance = balance
    
    @property
    def account_number(self):
        return self._account_number
    
    def get_account_name(self):     #dùng dạng phương thức
        return self._account_name

    @property       # getter, chuyển thành property - thuộc tính, cú pháp gọn hơn khi gọi ra, chỉ cần [classname].[propertyname]
    def balance(self):
        return self._balance

    @balance.setter
    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(self._account_number, self._account_name, self._balance), "đ"
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Amount < ballance or <= 0")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            return ValueError("amount < 0 ")

# phuongltx = BankAccount()
phuongltx = BankAccount(123, "Phương", 20000)       #gán value, tương tự set_details ở trên
phuongltx.display()
print("acc num =", phuongltx.account_number)
print("acc name =", phuongltx.get_account_name())
print("acc balance ban đầu =", phuongltx.balance)

phuongltx.withdraw(2000)
phuongltx.display()

phuongltx.deposit(1000)
phuongltx.display()
