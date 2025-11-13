def file_read(fname):
    # Ghi nội dung với encoding utf‑8
    with open(fname, "w", encoding="utf‑8") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")

    # Đọc lại với encoding utf‑8
    with open(fname, "r", encoding="utf‑8") as txt:
        print(txt.read())

file_read('abc.txt')
