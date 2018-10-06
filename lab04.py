import numpy as np
import itertools

def ct1(phrase, key, ret = ''):
	tmp = np.array(phrase)
	for item in key:
		ret+=str(item+1)
	for i in range(len(key)):
	    tmp[::,int(i)] = phrase[::,int(key[i])]
	return ret+' '+''.join(tmp.ravel())

def ct2(phrase, key, ret = ''):
	for item in key:
		ret+=str(item+1)
	tmp = np.array(phrase)
	for i in range(len(key)):
	    tmp[::,int(key[i])] = phrase[::,int(i)]
	tmp = tmp.T
	return ret+' '+''.join(tmp.ravel())

def encrypt(crypt, key):
	key = list(key)
	for i in range(len(key)):
		key[i] = int(key[i])-1
	crypt = np.array(list(crypt.replace(' ','')))
	return ct2(crypt.reshape(int(len(crypt)/len(key)),len(key)), key)

def decrypt(phrase, key, ret = ''):
	phrase = np.array(list(phrase))
	phrase = phrase.reshape(len(key),int(len(phrase)/len(key))).T
	if key.isdigit():
		key = list(map(int,key))
		for i in range(len(key)):
			key[i]-=1
		return ct1(phrase,key)
	else:
		key, num_arr, pos_arr = list(key), [i for i in range(len(key))], []
		for i in range(len(key)):
			if key[i].isdigit():
				key[i] = int(key[i])-1
				del num_arr[num_arr.index(key[i])]
		for i in range(len(key)):
			if key[i] == 'X':
				key[i] = num_arr.pop(0)
				num_arr.append(key[i]), pos_arr.append(i)
		mut = list(itertools.permutations(num_arr))
		for item in mut:
			for i in range(len(item)):
				key[pos_arr[i]] = item[i]
			ret+=ct1(phrase, key)+'\n'
		return ret

phrase = 'ЛЩЕОЬИЙМААТЛНТОАОЯСВКЗЕЗЛААТ'
crypt = 'ЛОКАЛЬНАЯ ЗАЩИТА СЕТЕЙ ОТ ВЗЛОМА'

print(encrypt(crypt,'7563124'))
print('-'*50)
print(decrypt(phrase, '7563124'))
print('-'*50)
print(decrypt(phrase, '7XX3X24'))
