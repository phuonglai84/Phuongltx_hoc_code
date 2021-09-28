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
        self.set_balance(balance)
    
    def set_balance(self, balance_new):
        if balance_new < 0:
            print("Acc ballance phải >0")
        else:
            self._balance = balance_new       
    
    def get_account_number(self):
        print("Acc number = ", self._account_number)
    
    def get_account_name(self):
        print("Acc name = ", self._account_name)

    def get_balance(self):
        print("Acc balance = ", self._balance)

    def display(self):
        print(self._account_number, self._account_name, self._balance)
    
    def withdraw(self, amount):
        self._balance -= amount
        print(self._balance)

    def deposit(self, amount):
        self._balance += amount
        print(self._balance)

# phuongltx = BankAccount()
phuongltx = BankAccount(123, "Phương", -10000)       #gán value, tương tự set_details ở trên
phuongltx.display()
phuongltx.get_account_number()
phuongltx.get_account_name()
phuongltx.get_balance()
phuongltx.withdraw(2000)
phuongltx.deposit(1000)