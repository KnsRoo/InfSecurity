import numpy as np

def readline(table, tmp, crypt, tgt):
	for index, item in np.ndenumerate(table):
		if item == 1: 
			if tgt: tmp[index[0]][index[1]] = crypt.pop(0)
			else: crypt+=tmp[index[0]][index[1]]
	return tmp, crypt		

def crypting(target, table, tmp):
	if target == 'encode': tmp, crypt, tgt = [list(map(str,table[i])) for i in range(len(table))], list(tmp.replace(' ','')), 1
	elif target == 'decode': tmp, crypt, tgt = np.array(list(tmp)).reshape(6,10), '', 0
	for i in range(4):
		tmp, crypt = readline(table, tmp, crypt, tgt)
		table = np.rot90(table,2) if i!=1 else np.fliplr(table)
	return ''.join((np.array(tmp)).ravel()) if target == 'encode' else crypt

if __name__ == "__main__":
	crypt = 'ШИФР РЕШЕТКА ЯВЛЯЕТСЯ ЧАСТНЫМ СЛУЧАЕМ ШИФРА МАРШРУТНОЙ ПЕРЕСТАНОВКИ'
	table = np.array([[0,1,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,1,1,0,0],[0,1,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,1,1,0,0,1]])
	phrase = crypting('encode', table, crypt)
	print(phrase+'\n'+crypting('decode',table, phrase))
