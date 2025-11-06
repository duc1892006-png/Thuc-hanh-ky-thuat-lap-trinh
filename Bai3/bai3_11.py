def benefit(t, n, k):
    # Công thức tính số tiền sau k tháng
    return n * (1 + t/100) ** k

t = float(input("Nhập lãi suất (%) mỗi tháng: "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng: {result:.2f}")
