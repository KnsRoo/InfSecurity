import sys, os, random, numpy as np
from PyQt5 import QtWidgets
from interface import Window

def readline(table, tmp, crypt, tgt):
	for index, item in np.ndenumerate(table):
		if item == 0: 
			if tgt: tmp[index[0]][index[1]] = crypt.pop(0)
			else: crypt+=tmp[index[0]][index[1]]
	return tmp, crypt       

def crypting(target, M, table, tmp):
	if target == 'encode': tmp, crypt, tgt = [list(map(str,table[i])) for i in range(len(table))], list(tmp.replace(' ','')), 1
	elif target == 'decode': tmp, crypt, tgt = np.array(list(tmp)).reshape(M), '', 0
	for i in range(4):
		tmp, crypt = readline(table, tmp, crypt, tgt)
		table = np.rot90(table,2) if i!=1 else np.fliplr(table)
	return ''.join((np.array(tmp)).ravel()) if target == 'encode' else crypt

def genmatrix(M, grid, pg, nul = False):
	array = list(np.arange(1,M[0]*M[1]+1))
	grid = np.array(array).reshape(M)
	if nul: return grid
	else:
	  larr = int(len(array)/4)
	  for i in range(larr):
	    pg.setValue(i/larr*100)
	    x,y = np.where(grid == random.choice(array))
	    array = list(set(array) - set([grid[x[0]][y[0]], grid[x[0]][M[1]-y[0]-1], grid[M[0]-x[0]-1][y[0]], grid[M[0]-x[0]-1][M[1]-y[0]-1]]))
	    grid[x[0]][y[0]] = 0
	pg.setValue(100)
	return grid

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window(genmatrix, crypting)
	mainWin.show()
	sys.exit(app.exec_())
