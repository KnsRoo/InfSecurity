import numpy as np
import re
import itertools

key = '7XX3X24'
key2 = list('7XX3X24')
key3 = [j for j in range(len(key))]
#print(key3)
phrase = 'ЛЩЕОЬИЙМААТЛНТОАОЯСВКЗЕЗЛААТ'
phrase = np.array(list(phrase))
key2 = np.array(key2)
phrase = phrase.reshape(int(len(phrase)/len(key2)),len(key2))
result = np.array(phrase)
print(phrase)
#print(result)

for i in range(len(key2)):
  if key2[i].isdigit():
    #print(key2[i])
    del key3[key3.index(int(key2[i])-1)]
    result[::,int(key2[i])-1] = phrase[::,i]

print(result)

a = list(itertools.permutations(key3))
print(a)

for x 
  for j in range(len(item)):
    result[::,x] = phrase[::,item[j]]

#for item in a:
#  for x in key3:
#    for j in range(len(item)):
#      result[::,x] = phrase[::,item[j]]
#      print(result)
