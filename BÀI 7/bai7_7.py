def count_lines_in_file(fname):
    try:
        with open(fname, 'r', encoding='utf‑8') as file:
            num_lines = sum(1 for _ in file)
        print(f"Số dòng trong tệp «{fname}»: {num_lines}")
    except FileNotFoundError:
        print(f"❌ Không tìm thấy tệp: {fname}")
    except Exception as e:
        print(f"⚠️ Có lỗi khi đọc tệp: {e}")

# Gọi hàm với tên tệp bạn muốn
count_lines_in_file('test.txt ')
