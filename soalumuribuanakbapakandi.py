## soal umur ibu dan anak
deltatahun1 = -19
deltatahun2 = 0
consdep1 = 1/4
consdep2 = 1/7
b1selisih = -1/2
b2selisih = 19

ui = (consdep1*deltatahun1 + b1selisih + b2selisih + deltatahun1) * (1/(consdep2-consdep1))
print(round(ui))

ua = consdep2 * ui + b2selisih
print(round(ua))
ulahir = 'anak lahir saat ibu berumur :', round(ui-ua)
print(ulahir)

## soal umur andi dan ayah

deltatahun1 = -4
deltatahun2 = 0
consdep1 = 6
consdep2 = 1
totalf1f2 = 50

andi = int((totalf1f2 - ((consdep1*deltatahun1) - deltatahun1))/(consdep1 +consdep2))

print(f'umur andi: {andi}')
ayah = round(totalf1f2 - andi)
print(f'umur ayah: {ayah}')
