import itertools, numpy as np

def crypting(phrase, key, tgt):
	tmp, ret = np.array(phrase), ''.join([str(item+1) for item in key ])
	for i, item in enumerate(key): tmp[::,i if tgt else int(item)] = phrase[::,int(item) if tgt else i]
	return ret+' '+''.join(tmp.ravel()) if tgt else ret+' '+''.join(tmp.T.ravel())

def encrypt(crypt, key):
	key, crypt = list(map(lambda x: int(x)-1,key)), np.array(list(crypt.replace(' ','')))
	return crypting(crypt.reshape(int(len(crypt)/len(key)),len(key)), key,0)

def decrypt(phrase, key, ret = ''):
	key = list(map(lambda x: int(x)-1,key)) if key.isdigit() else list(map(lambda x: str(int(x)-1) if x.isdigit() else x,key))
	if type(key[0]) is int: return crypting(phrase.reshape(len(key),int(len(phrase)/len(key))).T,key,1)
	else:
		num_arr, pos_arr = [i for i in range(len(key))], []
		for i, item in enumerate(key):
			if item.isdigit(): del num_arr[num_arr.index(int(key[i]))]
			else: num_arr.append(num_arr.pop(0)), pos_arr.append(i)
		for item in list(itertools.permutations(num_arr)):
			for i, num in enumerate(item): key[pos_arr[i]] = num
			ret+=crypting(phrase.reshape(len(key),int(len(phrase)/len(key))).T, list(map(int,key)),1)+'\n'
		return ret

if __name__ == "__main__":
  phrase, crypt = 'ЛЩЕОЬИЙМААТЛНТОАОЯСВКЗЕЗЛААТ','ЛОКАЛЬНАЯ ЗАЩИТА СЕТЕЙ ОТ ВЗЛОМА'
  try:
    with open('output.txt', 'w') as f:
      f.write(encrypt(crypt,'7563124')+'\n'+'-'*50+'\n'+decrypt(np.array(list(phrase)),'7563124')+'\n'+'-'*50+'\n'+decrypt(np.array(list(phrase)), 'XXXXXXX'))
  except ValueError: print('Size of phrase or key is invalid')
  finally: print('Success')
