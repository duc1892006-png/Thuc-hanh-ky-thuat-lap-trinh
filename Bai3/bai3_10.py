import math

def Tinh(R):
    if R <= 0:
        print("Bán kính không hợp lệ!")
        return
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    print(f"Chu vi: {chu_vi:.2f}")
    print(f"Diện tích: {dien_tich:.2f}")

R = float(input("Nhập bán kính hình tròn: "))
Tinh(R)
