def find_max_min_index(lst):
    max_value = max(lst)
    min_value = min(lst)
    max_index = lst.index(max_value)
    min_index = lst.index(min_value)
    return max_index, min_index

# Nhập giá trị từ bàn phím
lst = list(map(int, input("Enter a list of numbers: ").split()))

max_index, min_index = find_max_min_index(lst)
print(f"Max value found at index {max_index}")
print(f"Min value found at index {min_index}")
