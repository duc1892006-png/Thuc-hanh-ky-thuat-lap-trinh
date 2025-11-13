def find_longest_words(fname, encoding='utf‑8'):
    try:
        with open(fname, 'r', encoding=encoding) as file:
            content = file.read()
    except FileNotFoundError:
        print(f"❌ Không tìm thấy tệp: {fname}")
        return
    except UnicodeDecodeError as e:
        print(f"⚠️ Lỗi mã hóa khi đọc tệp {fname}: {e}")
        return

    words = content.split()
    if not words:
        print("Tệp rỗng hoặc không có từ nào.")
        return

    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    
    print(f"Những từ dài nhất (độ dài {max_length}): {', '.join(longest_words)}")

# Gọi hàm
find_longest_words('test.txt')
