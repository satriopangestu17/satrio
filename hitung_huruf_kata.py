## menghitung jumlah huruf tertentu dalam kalimat tanpa count()
nama = 'Hari ini Hari tidak masuk sekolah'
cari = 'h'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlcari = len(nama) - len(x)
print(jmlcari)
print(f'jumlah huruf \'{cari}\' ada = {jmlcari}')


cari = 'hari'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlcari = int(((len(nama)-len(x))/len(cari)))
print(f'jumlahkata \'{cari}\' ada = {jmlcari}')
