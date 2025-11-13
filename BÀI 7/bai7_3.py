def read_entire_file(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Không tìm thấy file: {fname}")
    except UnicodeDecodeError as e:
        print(f"Lỗi mã hóa khi đọc file: {e}")

read_entire_file('test.txt')
