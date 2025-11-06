import math

class Circle:
    def __init__(self, r):
        """Khởi tạo bán kính của hình tròn"""
        self.radius = r
        
    def area(self):
        """Tính diện tích hình tròn"""
        return math.pi * self.radius ** 2
    
    def circumference(self):
        """Tính chu vi hình tròn"""
        return 2 * math.pi * self.radius

# Tạo đối tượng Circle với bán kính 5
circle = Circle(5)

# In diện tích của hình tròn
print(f"Diện tích của hình tròn là: {circle.area()}")

# In chu vi của hình tròn
print(f"Chu vi của hình tròn là: {circle.circumference()}")
