import math, numpy as np

def createtable(key):
    table = np.array([list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ")])
    for i in range(len(table[0])-1):
        tmp = np.roll(table[len(table)-1],-1,axis=0)
        table = np.vstack((table,tmp))
    key = str(key*math.ceil((len(crypt))/len(key)))[:len(crypt)]
    return table, key

def encrypt(alp, table, key, crypt, phrase = ''):
    crypt = crypt.replace(' ','')
    for i in range(len(crypt)):
        m,n = alp.index(key[i]), alp.index(crypt[i])
        phrase+=table[m][n]
    return phrase

def decrypt(alp, table, key, crypt, phrase = ''):
    for i in range(len(crypt)):
        m = alp.index(key[i])
        x = np.where(table[m] == crypt[i])
        phrase+=alp[x[0][0]]
    return phrase

if __name__ == "__main__":
    alp, crypt, key = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ", 'МЫ ОТКРЫВАЕМ СЕБЯ', 'ПАРОЛЬ'
    table, key = createtable(key)
    phrase = encrypt(alp, table, key, crypt)
    print(phrase+'\n'+decrypt(alp, table, key, phrase))
