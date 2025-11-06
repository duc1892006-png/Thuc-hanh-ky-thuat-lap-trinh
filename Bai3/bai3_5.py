a = "Hello Guy!"

def say():
    global a
    a = " Vinh University "
    print(a)

say()  # In " Vinh University "
print(a)  # In " Vinh University "
