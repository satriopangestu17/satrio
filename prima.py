def prima(x):
    a = False
    if x > 1:
        if x == 2:
            a = True
        else:
            for i in range(2, x):  
                if x % i == 0:
                    a = False                  
                    break
                else:
                    a = True
    else: 
        a = False
    return a
print(prima(2))

#
nomor = range(101)
prime = list(filter(lambda x:(x%7 or x==7) and (x%5 or x == 5) and (x%3 or x==3) and (x%2 or x==2) and (x>1), nomor))
print(prime)

