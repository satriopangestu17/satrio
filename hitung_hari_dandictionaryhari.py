##hitung hari ke berapa:
hari = [ 'mon', 
'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

print(hari[0])

# sekarang hari wed, hari apakah 100 hari lagi?
now = 'wed'

day = 100


carihari = (hari.index(now) + day % len(hari)) % len (hari)

print (f'now', hari [carihari])
print ('now', hari [carihari])

##dictionary hari english to indo, indo to eng

days = {'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday',
'kamis': 'thursday', 'jumat': 'friday', 'sabtu': 'saturday', 
'minggu': 'sunday'}

ihari = list(days.keys())
eday = list(days.values())
namahari= input('ketiknamahari: ')

if namahari.lower() in ihari:
    indoeng = eday[ihari.index(namahari.lower())]
    print(f'{namahari.lower()} adalah {indoeng.lower()}')
else:
    engind = ihari[eday.index(namahari.lower())]
    print(f'{namahari.lower()} adalah {engind.lower()}')



