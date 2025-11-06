class ReverseString:
    def __init__(self, input_string):
        self.input_string = input_string
        
    def reverse(self):
        words = self.input_string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

# Đảo ngược chuỗi
input_string = 'hello .py'
reverser = ReverseString(input_string)
print(reverser.reverse())  # In ra '.py hello'
