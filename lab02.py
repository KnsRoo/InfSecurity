from collections import OrderedDict
from itertools import repeat
import numpy as np

def groupby(iterable, target):
    if target == 'encode':
        for i in range(0,len(iterable)-1,2):
            if iterable[i] == iterable[i+1]:
                iterable = iterable[:i+1]+'Ю'+iterable[i+1:]
        iterable+='Ю' if len(iterable) % 2 != 0 else ''
        reparr = ''.maketrans('ЙЬЁ','ИЪЕ')
        iterable = iterable.translate(reparr).replace(' ', '')
    return zip(*([iter(iterable)] * 2))

def crypting(target, alp, keyword, crypt, phrase = ''):
    z,f = 4 if target == 'encode' else 1, 5 if target == 'encode' else 1
    table = np.reshape(list(OrderedDict(zip(keyword + alp, repeat(None)))),(5,6))
    crypt = [''.join(i) for i in groupby(crypt,target)]
    for item in crypt:
        y1,x1 = np.where(table == item[0])
        y2,x2 = np.where(table == item[1])
        if x1 == x2: phrase+=table[y1[0]-z][x1[0]]+table[y2[0]-z][x2[0]]
        elif y1 == y2: phrase+=table[y1[0]][x1[0]-f]+table[y2[0]][x2[0]-f]
        else: phrase+=table[y1[0]][x2[0]]+table[y2[0]][x1[0]]
    return phrase

if __name__ == '__main__':
    alp, keyword  = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ", "ТОВАРИЩ"
    crypt = "КОД ПЛЕЙФЕЙЕРА ОСНОВАН НА ИСПОЛЬЗОВАНИИ МАТРИЦЫ БУКВ"
    phrase = "МОЩЕЯВЧЪЛТАПЯВМОМРЗФИЫПТБКВИХБЦБЩШЪЧШЩИВТЧОАДХОПАБТИВАРМЖИ" 
    print(crypting("encode", list(alp), list(keyword), crypt)+'\n'+crypting("decode", list(alp), list(keyword), list(phrase)))
