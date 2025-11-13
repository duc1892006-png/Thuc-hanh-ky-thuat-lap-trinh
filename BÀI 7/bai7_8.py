def write_list_to_file(fname, data_list):
    with open(fname, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")
    print(f"Đã viết vào tệp {fname}")

write_list_to_file('list.txt', ['Python', 'Java', 'C++'])
