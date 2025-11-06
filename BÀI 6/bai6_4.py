class RomanToInt:
    def __init__(self, roman):
        self.roman = roman
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        
    def convert(self):
        result = 0
        prev_value = 0
        for char in reversed(self.roman):
            value = self.roman_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

# Chuyển đổi số La Mã 'IX' thành số nguyên
roman_number = RomanToInt('IX')
print(roman_number.convert())  # In ra 9
