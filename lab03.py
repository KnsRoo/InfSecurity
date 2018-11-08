import math, numpy as np

def createtable(table, key, crypt):
    for i in range(len(table[0])-1):
        table = np.vstack((table,np.roll(table[len(table)-1],-1,axis=0)))
    return table, str(key*math.ceil((len(crypt))/len(key)))[:len(crypt)]

def crypting_visiner(target, alp, table, key, crypt, phrase = ''):
    return ''.join([table[alp.index(key[i]), alp.index(item)] if target == 'encode' else alp[np.asscalar(np.where(table[alp.index(key[i])] == crypt[i])[0])] for i, item in enumerate(crypt)])
    
def crypting_vernon(target, alp, key, crypt, phrase = ''):
    return ''.join([alp[(alp.index(crypt[i])+alp.index(key[i]))%32] if target == 'encode' else alp[(alp.index(crypt[i])-alp.index(key[i]))%32] for i, item in enumerate(crypt)])

alp, crypt, key = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ", 'МЫ ОТКРЫВАЕМ СЕБЯ', 'ПАРОЛЬ'
table, key = createtable(np.array([list(alp)]), key, crypt)
phrase = crypting_visiner('encode', alp, table, key, crypt.replace(' ',''))
print('------VISINER\n')
print(phrase+'\n'+crypting_visiner('decode', alp, table, key, phrase))
print('\n------VERNON\n')
phrase = crypting_vernon('encode', alp, key, crypt.replace(' ',''))
print(phrase+'\n'+crypting_vernon('decode', alp, key, phrase))
