from PIL import Image
import numpy as np

def align(str, p = 8):
	if len(str) == p: return str
	else: return align('0'+str, p)

def decode(crypt, shift):
	temp1, temp2, result = [], '', ''
	dec = np.asarray(Image.open(crypt))
	for index, item in np.ndenumerate(dec): temp1.append((bin(item)[2:])[-shift:])
	for item in temp1: temp2+=item[:shift]
	tmp = ''.join(temp2)
	answer = [''.join(i) for i in zip(*([iter(temp2)] * 8))]
	a = answer.pop(0)
	b = answer.pop(0)
	count = int(a+b,2)
	for j in range(count): result+=str(chr(int(answer[j],2)))
	return result

def encode(source, crypt, text, shift):
	temp1, temp2 = [], []
	File = Image.open(source)
	array = np.asarray(File)
	W,H = File.size
	text_size = len(text)
	for index, item in np.ndenumerate(array): temp1.append(bin(item)[2:])
	for item in text: temp2.append(bin(ord(item))[2:])
	temp1 = list(map(align,temp1))
	text_size = align(str(bin(text_size)[2:]), 16)
	temp2 = ''.join(text_size)+''.join(list(map(align,temp2)))
	temp3 = [''.join(i) for i in zip(*([iter(temp2)] * shift))]
	for i in range(len(temp3)): temp1[i] = (temp1[i])[:8-shift]+temp3[i]
	temp1 = np.array(list(map(lambda x:int(x,2),temp1))).reshape((H,W,3))
	result = Image.fromarray(np.uint8(temp1))
	result.save(crypt)

if __name__ == '__main__':
	source, crypt = 'in.bmp', 'out.bmp'
	text, shift = 'Hello. My name is Ilya', 2
	encode(source, crypt, text, shift)
	print(decode(crypt, shift))