
# #balik kata dalam kalimat
# nama = 'hai aku lintang'
# namasplit = nama.split()
# print(namasplit)

# def ngebalik(l):
#     namadibalikin = ''
#     for t in l:
#         balik = t[::-1] + ' '
#         namadibalikin+= balik  
#     return namadibalikin

# print(ngebalik(namasplit))


# #ngebalik dengan fungsi
# y = [3,5,7,9]
# def balikposisi(mylist):
#     for e in range(round(len(mylist)/2)): #dibagi 2 untuk tengah2ny
#         asli = mylist[e] # e tengahnya sama
#         mylist[e] = mylist[len(mylist)-1-e]
#         mylist[len(mylist)-1-e] = asli
#     return mylist
# print(balikposisi(y))

x = [2,4,6,8,10]
b= []
for i in x:
    b.append(i ** 2)
print(b)

g = [1,2,3]
g.append(g*2)
print(g)