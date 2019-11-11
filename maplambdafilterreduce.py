##reduce
nomor = range(1,101,1)
t = list(map(lambda z: z*2, filter(lambda z: z%2 ==0, nomor)))
print(t)
from functools import reduce
t = reduce(lambda  x,y: x+y, t)
print(t)

##map then filter
angka = [1,2,3,4]
z = list(filter(lambda x: x%2==0, map(lambda x: x*2, angka)))
print(z)