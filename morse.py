##morse
morse = {'a':'._', 'b':'_...', 'c':'_._.', 'd': '_..', 'e':'.',
'f':'.._.','g':'__.','h':'....','i':'..','j':'.__','k':'_._','l':'._..',
'm':'__','n':'_.','o':'___','p':'.__.','q':'__._','r':'._.','s':'...',
't':'_','u':'.._','v':'..._','w':'.__','x':'_.._','y':'_.__','z':'__..',' ':'/'}
kata = 'satrio pangestu'

def getmorse(p):
    tulisanmorse = ''
    for i in kata:
        tulis = morse[i]
        tulisanmorse += tulis + ' '
    return tulisanmorse
print(getmorse(kata))