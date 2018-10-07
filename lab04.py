import itertools, numpy as np

def crypting(tgt, phrase, key):
	tmp, ret = np.array(phrase), ''.join([str(item+1) for item in key ])
	for i in range(len(key)):
		m,k = int(i) if tgt else int(key[i]), int(key[i]) if tgt else int(i)
		tmp[::,m] = phrase[::,k]
	return ret+' '+''.join(tmp.ravel()) if tgt else ret+' '+''.join(tmp.T.ravel())

def encrypt(crypt, key):
	key, crypt = list(map(lambda x: int(x)-1,key)), np.array(list(crypt.replace(' ','')))
	return crypting(0,crypt.reshape(int(len(crypt)/len(key)),len(key)), key)

def decrypt(phrase, key, ret = ''):
	phrase = np.array(list(phrase))
	if key.isdigit():
		key = list(map(lambda x: int(x)-1,key))
		return crypting(1,phrase.reshape(len(key),int(len(phrase)/len(key))).T,key)
	else:
		key, num_arr, pos_arr = list(key), [i for i in range(len(key))], []
		for i in range(len(key)):
			if key[i].isdigit():
				key[i] = int(key[i])-1
				del num_arr[num_arr.index(key[i])]
			else:
				key[i] = num_arr.pop(0)
				num_arr.append(key[i]), pos_arr.append(i)
		for item in list(itertools.permutations(num_arr)):
			for i in range(len(item)):
				key[pos_arr[i]] = item[i]
			ret+=crypting(1,phrase.reshape(len(key),int(len(phrase)/len(key))).T, key)+'\n'
		return ret

if __name__ == "__main__":
	phrase, crypt = 'ЛЩЕОЬИЙМААТЛНТОАОЯСВКЗЕЗЛААТ','ЛОКАЛЬНАЯ ЗАЩИТА СЕТЕЙ ОТ ВЗЛОМА'
	try:
		print(encrypt(crypt,'7563124')+'\n'+'-'*50+'\n'+decrypt(phrase, '7563124')+'\n'+'-'*50+'\n'+decrypt(phrase, '7XX3X24'))
	except ValueError:
		print('Size of phrase or key is invalid')
