# x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1]

# # def bubbleSort(list) :
# #     for i in range(len(list), 0, -1) :
# #         for j in range(0,i-1) :
# #             if (list[j] > list[j + 1]) :
# #                 temp = list[j]
# #                 list[j] = list[j + 1]
# #                 list[j + 1] = temp
# #     return list
# # print(bubbleSort(x))

# def bubblesort(list):
#     for i in range(len(list), 0, -1):
#         # print(i)
#         for j in range(0, i-1): #kenapa i dikurang 1 dan plus 1, untuk membandingkan misal yang urutan 1 dengan 2 gedean mana
#             print(j)
#             if (list[j] > list[j+1]):
#                 # print (list[j+1])
#                 temp = list[j]
#                 list[j]=list[j+1]
#                 list[j+1] = temp
#     return list  ##yang dipanggil list nya lagi karena list nya yang diedit. ngga bikin variabel baru

# print(bubblesort(x))



# ##cara ngebalik yang benar
# z = [12,23,13,53,3,10]
# # zbal = (z[::-1]) ##kenapa listi[::-1] ga bisa dibalik didalam def? karena int ga bisa dibolakbalik ketika sudah dilist kebawah by for. di dalam for setiap komponen angka satu persatu di balik sendiri2 haru di str. bisa dibalik didalem atau diluar fungsi for
# def ngebalik(a):
#     hasil = []
#     for i in range(len(z)):
#         listi = z[i] ###dengan ada listi tidak ada perbedaan apabila dengan ditiadakan listi
#         balik = z[::-1] #bukan listi[i] kerana ga bakal bisa dibalik
#         # print(balik)
#         # print(listi)   
#         hasil.append(balik)
#     return hasil[0]

# print(ngebalik(z))


# # def bubblesort(list):
# #     for j in range(0, list-1): ##wrong list-1
# #         # print(j)
# #         if (list[j] > list[j+1]):
# #             print (list[j+1])
# #             temp = list[j]
# #             list[j]=list[j+1]
# #             list[j+1] = temp
# #     return list  ##yang dipanggil list nya lagi karena list nya yang diedit

# # print(bubblesort(x))


# # a = [1,2,3,4]
# # baru = a[2]
# # a[2] = a[3]
# # a[3] = a

# # print(a)

# hari = {'senin':'monday', 'selasa':'tuesday', 'rabu':'wednesday',
# 'kamis':'thursday', 'jumat':'friday', 'sabtu':'saturday', 'minggu':'sunday'}

# listhari = list(hari.keys())
# listday = list(hari.values())

# inputnama = 'SENIN'

# if inputnama.lower() in listhari:
#     indotoeng = listday[listhari.index(inputnama.lower())]
#     print(f'{inputnama} adalah {indotoeng}')
# else:
#     engtoindo = listhari[listday.index(inputnama.lower())]
#     print(f'{inputnama.lower()} adalah {engtoindo}')


# inputke = 0
# batasinput = 5
# password = '12345'
# inputpass = 2
# lebih = False

# while inputpass != password and not lebih:
#     if inputke < batasinput:
#         inputpass = input(f'inputan ke-{inputke+1} ')
#         inputke += 1
#     else:
#         lebih =True
# if not lebih:
#     print('password anda benar')
# else:
#     print('password anda salah silahkan coba lagi dalam 24 jam')

#cesarcipher

# alphabet = ['a','b','c','d','e','f','g','h','i',
# 'j','k','l','m','n','o','p','q','r','s','t','u','v','w',
# 'x','y','z']

# tulisan = 'abz'

# def cesar(x):
#     hasil = ''
#     for i in x:
#         b = alphabet.index(i)
#         c = alphabet[(b+2)%len(alphabet)]
#         hasil += c

#     return hasil
# print (cesar(tulisan))

class karnivora:
    def __init__ (self):
        self.daging = 'daging'

class herbivora:
    def __init__ (self):
        self.tumbuhan = 'tumbuhan'

class omnivora(karnivora,herbivora):
    def __init__ (self):
        karnivora.__init__(self)
        herbivora.__init__(self)
        self.mcd = 'burger'

obja = omnivora()
print(obja.mcd)
print(vars(obja))







        



