def faktorial(x):
    angka = 1 
    for i in range(1, x+1):
        angka *= i
    return angka
print(faktorial(4))

def faktorial2(x):
    if x <= 2:
        return x
    else:
        return x * faktorial2(x-1) 
print(faktorial2(5))