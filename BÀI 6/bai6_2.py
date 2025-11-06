class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def area(self):
        return self.dai * self.rong

# Tạo đối tượng Hinhchunhat với chiều dài 5 và chiều rộng 3
aHinhchunhat = Hinhchunhat(5, 3)
print(aHinhchunhat.area())  # In diện tích hình chữ nhật
