import numpy as np
import math

alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
crypt = 'МЫ ОТКРЫВАЕМ СЕБЯ'
key = 'ПАРОЛЬ'

table = np.array([list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ")])
for i in range(len(table[0])-1):
    tmp = np.roll(table[len(table)-1],-1,axis=0)
    table = np.vstack((table,tmp))

def encrypt(crypt, phrase = ''):
    global key
    crypt = crypt.replace(' ','')
    key = str(key*math.ceil((len(crypt))/len(key)))[:len(crypt)]
    for i in range(len(crypt)):
        m,n = alp.index(key[i]), alp.index(crypt[i])
        phrase+=table[m][n]
    return phrase

def decrypt(crypt, phrase = ''):
    for i in range(len(crypt)):
        m = alp.index(key[i])
        x = np.where(table[m] == crypt[i])
        phrase+=alp[x[0][0]]
    return phrase

phrase = encrypt(crypt)
print(phrase)
print(decrypt(phrase))
