import math, numpy as np

def createtable(table, key):
    for i in range(len(table[0])-1):
        table = np.vstack((table,np.roll(table[len(table)-1],-1,axis=0)))
    return table, str(key*math.ceil((len(crypt))/len(key)))[:len(crypt)]

def crypting(target, alp, table, key, crypt, phrase = ''):
    for i, item in enumerate(crypt):
        m = alp.index(key[i])
        n = alp.index(item) if target == 'encode' else np.where(table[m] == crypt[i])
        phrase+=table[m][n] if target == 'encode' else alp[n[0][0]]
    return phrase

if __name__ == "__main__":
    alp, crypt, key = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ", 'МЫ ОТКРЫВАЕМ СЕБЯ', 'ПАРОЛЬ'
    table, key = createtable(np.array([list(alp)]), key)
    phrase = crypting('encode', alp, table, key, crypt.replace(' ',''))
    print(phrase+'\n'+crypting('decode', alp, table, key, phrase))
