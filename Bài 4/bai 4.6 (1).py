import binary_search_module

n = int(input("Nhập số lượng phần tử: "))
my_list = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    my_list.append(value)

value = int(input("Nhập phần tử cần tìm: "))

result = binary_search_module.binary_search(my_list, value)
print(f"Kết quả tìm kiếm: {result}")