class StringHandler:
    def get_String(self):
        """Chấp nhận một chuỗi từ người dùng."""
        self.user_string = input("Nhập chuỗi: ")
    
    def print_String(self):
        """In chuỗi đã nhập bằng chữ in hoa."""
        print(self.user_string.upper())

# Tạo đối tượng của class StringHandler
handler = StringHandler()

# Gọi phương thức get_String để nhập chuỗi từ người dùng
handler.get_String()

# Gọi phương thức print_String để in chuỗi đã nhập bằng chữ in hoa
handler.print_String()
