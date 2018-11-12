from PIL import Image
import numpy as np

def align(str, p = 8):
	return str if len(str) == p else align('0'+str, p)

def openf(source):
	File = Image.open(source); W,H = File.size
	return np.asarray(File), W,H

def decode(crypt, shift):
	temp1 = [align(bin(item)[2:])[-shift:] for index, item in np.ndenumerate(np.asarray(Image.open(crypt)))]
	temp2 = ''.join([item[:shift] for item in temp1])
	answer = [''.join(i) for i in zip(*([iter(temp2)] * 8))]
	return ''.join([chr(int(answer[j],2)) for j in range(int(answer.pop(0)+answer.pop(0),2))])

def encode(source, crypt, text, shift):
	array, W, H = openf(source)
	if len(text)*4 > 3*W*H: return print('Text too long for this image')
	temp1 = [align(bin(item)[2:]) for index, item in np.ndenumerate(array)]
	temp2 = [align(bin(ord(item))[2:]) for item in text]
	temp3 = [''.join(i) for i in zip(*([iter(''.join(align(str(bin(len(text))[2:]), 16))+''.join(temp2))] * shift))]
	for i in range(len(temp3)): temp1[i] = (temp1[i])[:8-shift]+temp3[i]
	Image.fromarray(np.uint8(np.array(list(map(lambda x:int(x,2),temp1))).reshape((H,W,3)))).save(crypt)
	return 'sucess'

if __name__ == '__main__':
	source, crypt, shift = 'in.bmp', 'out.bmp', 2
	with open('text.txt') as f: text = f.read()
	if (encode(source, crypt, text, shift)) == 'sucess': print(decode(crypt, shift))