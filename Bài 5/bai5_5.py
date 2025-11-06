def find_max_min(lst):
    max_value = max(lst)
    min_value = min(lst)
    return max_value, min_value

# Nhập giá trị từ bàn phím
lst = list(map(int, input("Enter a list of numbers: ").split()))

max_value, min_value = find_max_min(lst)
print("Max value:", max_value)
print("Min value:", min_value)
