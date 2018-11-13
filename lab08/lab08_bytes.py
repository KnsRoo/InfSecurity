from PIL import Image
import numpy as np

def openf(source):
	File = Image.open(source); W,H = File.size
	return np.asarray(File), W,H

def encode(source, crypt, text, shift, step):
	cmap, W, H = openf(source)
	cmap = cmap.ravel()
	cmap.setflags(write = 1)
	bytearr, j, mask = [], 0, (255 >> shift) << shift
	switch = { '1' : 1, '2': 3, '4': 15, '8' }
	m = switch[str(shift)]
	for item in [ len(text) // 256 , len(text) % 256]: 
		if shift != 8:
			for i in range(8, 0, -shift):
				bytearr.append((item >> i-shift) & m)
		else: bytearr.append(item)
	for item in text: 
		if shift != 8:
			for i in range(8, 0, -shift):
				bytearr.append((ord(item) >> i-shift) & m)
		else: bytearr.append(ord(item))
	for i in range(0,len(bytearr)*step, step):
		if shift != 8: cmap[i] = (cmap[i] & mask) + bytearr[j]
		else: cmap[i] = bytearr[j]
		j+=1
	Image.fromarray(np.uint8(cmap.reshape((H,W,3)))).save(crypt)

def decode(crypt, shift, step):
	cmap = np.asarray(Image.open(crypt)).ravel()
	cmap.setflags(write = 1)
	bytearr, res, lg, tmp = [], '', [], None
	switch = { '1' : 1, '2': 3, '4': 15 }
	m = switch[str(shift)]
	for item in cmap:
		if shift != 8: bytearr.append((item >> 0) & m)
		else: bytearr.append(item)
	for i in range(0, int(16/shift)*step, int(8/shift)*step):
		if shift!= 8:
			tmp0 = (bytearr[i] << shift) + bytearr[i+1*step]
			for j in range(2,int(8/shift),1):
				tmp0 = (tmp0 << shift) + bytearr[i+j*step]
			lg.append(tmp0)
		else: lg = [bytearr[0], bytearr[step]]
	for i in range(int(16/shift)*step,int(16/shift)*step+(lg[0]*256+lg[1])*step*int(8/shift),int(8/shift)*step):
		if shift != 8:
			tmp0 = (bytearr[i] << shift) + bytearr[i+1*step]
			for j in range(2,int(8/shift),1):
				tmp0 = (tmp0 << shift) + bytearr[i+j*step]
		else: tmp0 = bytearr[i]
		res+=chr(tmp0)
	return res

if __name__ == '__main__':
	source, crypt, shift, step = 'in.bmp', 'out.bmp', 4, 4
	with open('text.txt') as f: text = f.read()
	try:
		encode(source, crypt, text, shift, step)
		print(decode(crypt, shift, step))
	except IndexError: print('Text size too long')