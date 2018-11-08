from collections import OrderedDict
from itertools import repeat
import numpy as np

def groupby(iterable, target):
    if target == 'encode':
        for i in range(0,len(iterable)-1,2):
            if iterable[i] == iterable[i+1]: iterable = iterable[:i+1]+'Ю'+iterable[i+1:]
        if len(iterable) % 2 != 0: iterable+='Ю' 
        iterable = iterable.translate(''.maketrans('ЙЬЁ','ИЪЕ')).replace(' ', '')
    return zip(*([iter(iterable)] * 2))

def crypting(target, alp, keyword, crypt, phrase = ''):
    z, f = (4, 5) if target == 'encode' else (1, 1)
    table = np.reshape(list(OrderedDict(zip(keyword + alp, repeat(None)))), (5,6))
    crypt = [''.join(i) for i in groupby(crypt,target)]
    print(crypt)
    for i, j in crypt:
        y1, x1 = list(map(np.asscalar, np.where(table == i)))
        y2, x2 = list(map(np.asscalar, np.where(table == j)))
        if x1 == x2: phrase+=table[y1-z][x1]+table[y2-z][x2]
        elif y1 == y2: phrase+=table[y1][x1-f]+table[y2][x2-f]
        else: phrase+=table[y1][x2]+table[y2][x1]
    return phrase

if __name__ == '__main__':
    alp, keyword  = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ", "ТОВАРИЩ"
    crypt = "КОД ПЛЕЙФЕЙЕРА ОСНОВАН НА ИСПОЛЬЗОВАНИИ МАТРИЦЫ БУКВ"
    phrase = "МОЩЕЯВЧЪЛТАПЯВМОМРЗФИЫПТБКВИХБЦБЩШЪЧШЩИВТЧОАДХОПАБТИВАРМЖИ" 
    print(crypting("encode", list(alp), list(keyword), crypt)+'\n'+crypting("decode", list(alp), list(keyword), list(phrase)))
