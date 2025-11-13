import os

def file_read_from_tail(fname, lines, encoding='utf‑8'):
    try:
        fsize = os.stat(fname).st_size
    except OSError as e:
        print(f"Không thể truy cập tệp {fname}: {e}")
        return
    
    if fsize == 0:
        print("Tệp rỗng.")
        return

    bufsize = 8192
    if bufsize > fsize:
        bufsize = fsize

    data = []
    with open(fname, 'r', encoding=encoding, errors='replace') as f:
        iter = 1
        while True:
            # Tính vị trí seek, đảm bảo ≥ 0
            offset = fsize - bufsize * iter
            if offset < 0:
                offset = 0
            f.seek(offset)
            chunk = f.readlines()  # đọc các dòng từ vị trí đó tới cuối
            data = chunk + data  # thêm lên đầu danh sách hiện có
            if len(data) >= lines or offset == 0:
                # In ra các dòng cuối
                for line in data[-lines:]:
                    print(line, end='')
                break
            iter += 1

# Gọi hàm
file_read_from_tail('test.txt', 2)


