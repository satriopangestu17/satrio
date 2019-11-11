#memangkatkan angka dengan fungsi
def pangkat(x,y):
    out = 1
    for i in range(y):
        out *= x 
    print(out)
pangkat(3,3)
