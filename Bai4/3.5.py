
print("##################################")
ds = input('danh sach:').split()

# in ca day vua nhap
print(ds)

# in day vua nhap , moi phan tu tren mot dong
for so in ds:
    print(so)

# in day vua nhap thao thu tu nguoc lai
ds.reverse()
print(' '.join(ds))
