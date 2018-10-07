import numpy as np

def readline(table, tmp, crypt, tgt):
	for i in range(len(table)):
		for j in range(len(table[0])):
			if table[i][j] == 1:
				if tgt:
					tmp[i][j] = crypt.pop(0)
				else:
					crypt+=tmp[i][j]
	return tmp, crypt

def crypting(target, table, tmp):
	if target == 'encode':
		tmp, crypt, tgt = [list(map(str,table[i])) for i in range(len(table))], list(tmp.replace(' ','')), 1
	elif target == 'decode':
		tmp, crypt, tgt = np.array(list(tmp)).reshape(6,10), '', 0
	tmp, crypt = readline(table, tmp, crypt, tgt)
	table = np.rot90(table,2)
	tmp, crypt = readline(table, tmp, crypt, tgt)
	table = np.fliplr(table)
	tmp, crypt = readline(table, tmp, crypt, tgt)
	table = np.rot90(table,2)
	tmp, crypt = readline(table, tmp, crypt, tgt)
	return ''.join((np.array(tmp)).ravel()) if target == 'encode' else crypt

if __name__ == "__main__":
	crypt = 'ШИФР РЕШЕТКА ЯВЛЯЕТСЯ ЧАСТНЫМ СЛУЧАЕМ ШИФРА МАРШРУТНОЙ ПЕРЕСТАНОВКИ'
	table = np.array([[0,1,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,1,1,0,0],[0,1,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,1,1,0,0,1]])
	phrase = crypting('encode', table, crypt)
	print(phrase+'\n'+crypting('decode',table, phrase))
