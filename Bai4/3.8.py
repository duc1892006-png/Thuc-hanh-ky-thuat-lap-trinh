
print("##################################")
# nhap day cac tu tu ban pgim, tach chung thanh danh sach
word_list = input("nhap day cac tu, cach nhau bang dau cach: ").split()

# tim va in ra tu dai nhat va moi tu co cung do dai nhat
if word_list:
    max_length = max(len(word) for word in word_list)
    longest_words =[word for word in word in word_list  if len(word) ==max_length]
    print("tu dai nhat trong cung day:", longest_words[0])
    print("cac tu co cung do dai nhat:", ", ".join(longest_words))
else:
    print("khong co tu nao trong day.")
    
