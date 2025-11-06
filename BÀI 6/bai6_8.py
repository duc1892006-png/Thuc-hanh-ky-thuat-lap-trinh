class ATM:
    def __init__(self, balance=0):
        """Khởi tạo tài khoản với số dư mặc định (0 hoặc giá trị được nhập)"""
        self.balance = balance

    def deposit(self, amount):
        """Nạp tiền vào tài khoản"""
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} vào tài khoản.")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        """Rút tiền từ tài khoản"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Đã rút {amount} từ tài khoản.")
        else:
            print("Số dư không đủ hoặc số tiền rút không hợp lệ.")

    def check_balance(self):
        """Kiểm tra số dư tài khoản"""
        print(f"Số dư hiện tại của bạn là: {self.balance}.")

# Tạo đối tượng ATM với số dư ban đầu là 1000
atm = ATM(1000)

# Hiển thị menu
while True:
    print("\n--- Menu ATM ---")
    print("1. Nạp tiền")
    print("2. Rút tiền")
    print("3. Kiểm tra số dư")
    print("4. Thoát")
    
    choice = input("Chọn một tùy chọn (1/2/3/4): ")
    
    if choice == '1':
        amount = floatinput

