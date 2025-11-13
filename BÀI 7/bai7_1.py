def reverse_file_content(fname):
    with open(fname, 'r') as file:
        content = file.read()
        print(content[::-1])
