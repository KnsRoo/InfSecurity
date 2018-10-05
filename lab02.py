from collections import OrderedDict
from itertools import repeat
import numpy as np
import string as st

alp = list("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ")
keyword = list("ТОВАРИЩ")
crypt = "КОД ПЛЕЙФЕЙЕРА ОСНОВАН НА ИСПОЛЬЗОВАНИИ МАТРИЦЫ БУКВ"
phrase = list("МОЩЕЯВЧЪЛТАПЯВМОМРЗФИЫПТБКВИХБЦБЩШЪЧШЩИВТЧОАДХОПАБТИВАРМЖИ")

def groupby(iterable, target):
	if target == 'encode':
		for i in range(0,len(iterable)-1,2):
			if iterable[i] == iterable[i+1]:
				iterable = iterable[:i+1]+'Ю'+iterable[i+1:]
		if len(iterable) % 2 != 0:
			iterable+='Ю'
		reparr = [[' ','Й','Ь','Ё'],
		 	 ['', 'И','Ъ','Е']]
		for i in range(len(reparr[0])):
			iterable = iterable.replace(reparr[0][i], reparr[1][i])
	args = [iter(iterable)] * 2
	return zip(*args)

def crypting(target,crypt):
	if target == 'encode':
		z,f = 4,5
	elif target == 'decode':
		z,f = 1,1
	else:
		return 'target is invalid'
	table = np.reshape(list(OrderedDict(zip(keyword + alp, repeat(None)))),(5,6))
	crypt = [''.join(i) for i in groupby(crypt,target)]
	phrase = ''
	for item in crypt:
		y1,x1 = np.where(table == item[0])
		y2,x2 = np.where(table == item[1])
		if x1 == x2:
			phrase+=table[y1[0]-z][x1[0]]+table[y2[0]-z][x2[0]]
		elif y1 == y2:
			phrase+=table[y1[0]][x1[0]-f]+table[y2[0]][x2[0]-f]
		else:
			phrase+=table[y1[0]][x2[0]]+table[y2[0]][x1[0]]
	return phrase

print(crypting("encode", crypt))
print(crypting("decode", phrase))
