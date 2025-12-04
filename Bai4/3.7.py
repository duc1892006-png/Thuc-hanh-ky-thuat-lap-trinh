
print("##################################")
# nhap chuoi tu ban phim
input_string = input("nhap chuoi:")

# su dung phuong thuc isalpha() de loai bo chu so
new_string = ''.join(char for char in input_string if char.isalpha())

# in noi dung chuoi moi sau khi loai bo cac chu so
print("chuoi moi sau khi loai bo cac chu so:", new_string)
