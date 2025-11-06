class Circle:
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        return self.radius**2 * 3.14

# Tạo đối tượng Circle với bán kính là 2
aCircle = Circle(2)
print(aCircle.area())  # In diện tích của hình tròn
