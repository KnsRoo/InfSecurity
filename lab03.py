import math, numpy as np

def createtable(table, key, crypt):
    for i in range(len(table[0])-1):
        table = np.vstack((table,np.roll(table[len(table)-1],-1,axis=0)))
    return table, str(key*math.ceil((len(crypt))/len(key)))[:len(crypt)]

def crypting_visiner(target, alp, table, key, crypt, phrase = ''):
    for i, item in enumerate(crypt):
        m = alp.index(key[i])
        n = alp.index(item) if target == 'encode' else np.where(table[m] == crypt[i])
        phrase+=table[m][n] if target == 'encode' else alp[n[0][0]]
    return phrase
    
def crypting_vernon(target, alp, key, crypt, phrase = ''):
    for i, item in enumerate(crypt):
        m, n = alp.index(crypt[i]), alp.index(key[i])
        n = n if target == 'encode' else -n
        phrase+=alp[(m+n)%32]
    return phrase

alp, crypt, key = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ", 'МЫ ОТКРЫВАЕМ СЕБЯ', 'ПАРОЛЬ'
table, key = createtable(np.array([list(alp)]), key, crypt)
phrase = crypting_visiner('encode', alp, table, key, crypt.replace(' ',''))
print('------VISINER\n')
print(phrase+'\n'+crypting_visiner('decode', alp, table, key, phrase))
print('\n------VERNON\n')
phrase = crypting_vernon('encode', alp, key, crypt.replace(' ',''))
print(phrase+'\n'+crypting_vernon('decode', alp, key, phrase))
