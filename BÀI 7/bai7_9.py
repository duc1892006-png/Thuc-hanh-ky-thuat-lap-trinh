def copy_file_content(source, destination, encoding='utf‑8'):
    try:
        with open(source, 'r', encoding=encoding) as src:
            content = src.read()
    except FileNotFoundError:
        print(f"❌ Không tìm thấy tệp nguồn: {source}")
        return
    except UnicodeDecodeError as e:
        print(f"⚠️ Lỗi mã hóa khi đọc tệp {source}: {e}")
        return

    try:
        with open(destination, 'w', encoding=encoding) as dest:
            dest.write(content)
    except Exception as e:
        print(f"❌ Có lỗi khi ghi vào tệp {destination}: {e}")
        return

    print(f"✅ Đã sao chép nội dung từ {source} sang {destination}")

# Gọi:
copy_file_content('source.txt', 'destination.txt')
