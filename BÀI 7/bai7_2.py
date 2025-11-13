def file_stats(fname):
    with open(fname, 'r') as file:
        content = file.read()
        num_chars = len(content)
        num_words = len(content.split())
        num_lines = len(content.splitlines())
        
    print(f"Số ký tự: {num_chars}")
    print(f"Số từ: {num_words}")
    print(f"Số dòng: {num_lines}")

file_stats('test.txt')
