#Konversi Nilai

#nilai >= 82 : a
#nilai 72-81 : b
#....

nilai = 92
##
if nilai >= 82:
    print ('a')
elif nilai >= 72 and nilai <= 81:
    print('b')
elif nilai >= 62 and nilai <= 71:
    print('c')
elif nilai >= 52 and nilai <= 61:
    print ('d')
else:
    print ('e')

#Cek ganjil genap:
def gangen(angka):
    if angka % 2 == 0:
        return 'genap'
    else:
        return 'ganjil'

print(gangen(30))

def ganjilgenap(x):
    if float(x%2) == float(0):   
        print (f'{x} adalah genap')
    else:
        print (f'{x} adalah ganjil')
ganjilgenap (2)

#pangkat dan kuadrat:
def kuadrat(x): 
    print(x**2)
kuadrat(2)
kuadrat(3)

#operasi dengan input User:
def pangkat(angka1, angka2):
    print(angka1 ** angka2)
pangkat(float(input('ketik angkat1: ')), float(input('ketik angka2: ')))




#ubah huruf vokal menjadi o
def vocal(kalimat):
    kalimat  = kalimat.lower()
    kalimat  = kalimat.replace('a','o')
    kalimat  = kalimat.replace('i','o')
    kalimat  = kalimat.replace('u','o')
    kalimat  = kalimat.replace('e','o')
    kalimat  = kalimat.replace('o','o')
    print(kalimat)
vocal('KUda')



##palindrom
def palindrome2(kata):
    for i in range(round(len(kata)/2)):
        palindromekah = False
        if kata[i] == kata[len(kata)-1-i]:
            palindromekah = True
        else:
            palindromekah = False
            break 
    return palindromekah
print(palindrome2('katak'))

