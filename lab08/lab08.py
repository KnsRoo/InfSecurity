from PIL import Image
import numpy as np

def align(str, p = 8):
	return str if len(str) == p else align('0'+str, p)

def decode(crypt, shift):
	temp1, temp2, result = [], '', ''
	dec = np.asarray(Image.open(crypt))
	for index, item in np.ndenumerate(dec): temp1.append(align(bin(item)[2:]))
	for i in range(len(temp1)): temp1[i] = temp1[i][-shift:]
	for item in temp1: temp2+=item[:shift]
	answer = [''.join(i) for i in zip(*([iter(temp2)] * 8))]
	a = answer.pop(0); b = answer.pop(0)
	count = int(a+b,2)
	for j in range(count): result+=str(chr(int(answer[j],2)))
	return result

def encode(source, crypt, text, shift):
	temp1, temp2 = [], []
	File = Image.open(source)
	array = np.asarray(File)
	W,H = File.size
	if len(text)*4 > 3*W*H: return print('Text too long for this image')
	for index, item in np.ndenumerate(array): temp1.append(align(bin(item)[2:]))
	for item in text: temp2.append(bin(ord(item))[2:])
	text_size = align(str(bin(len(text))[2:]), 16)
	temp3 = [''.join(i) for i in zip(*([iter(''.join(text_size)+''.join(list(map(align,temp2))))] * shift))]
	for i in range(len(temp3)): temp1[i] = (temp1[i])[:8-shift]+temp3[i]
	temp1 = np.array(list(map(lambda x:int(x,2),temp1))).reshape((H,W,3))
	result = Image.fromarray(np.uint8(temp1))
	result.save(crypt)
	return 'sucess'

if __name__ == '__main__':
	source, crypt, shift = 'in.bmp', 'out.bmp', 2
	with open('text.txt') as f: text = f.read()
	if (encode(source, crypt, text, shift)) == 'sucess':
		print(decode(crypt, shift))