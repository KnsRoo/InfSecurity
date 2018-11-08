# Laboratory work №1

This is one of the classic algorithms - Cesar Algorithm.

## Principle:

Shift each symbol in line for k. 

### Example

Let alphabet = 'abcd', let line = 'abcd'

| a | b | c | d |   |
|---|---|---|---|---|

for k = 1:
| a | b | c | d |  |
|---|---|---|---|---| ->
| b | c | d |a |  |
|---|---|---|---|---|


for k = 2:

| a | b | c | d | -> | c | d | a | b |

Back by analogy

## coding

Function crypting can code and decode line. It determined by "target" variable. Function accept values:

* target - st, can be 'encode' or 'decode';
* alp - str, current alphabet for coding, decoding;
* crypt - str, line, which needs in coding or decoding;
* k_and_f - (int, list), shift if encoding, or filter of bigrams if decoding;
* ret = '' - str, initial line for return.

###Details:

```
alp = 'abcd'
crypt = 'abcd'
k = 1 #shift
size = len(crypt) # length of crypt
alp_size = len(alp) # length of alphabet
ret = '' # answer
for i in range(size):
      symbol = crypt[i] #current symbol with shift
      index = alp.index(symbol) # index symbol in alp
      newindex = (index + k) % 4 # index of shifted symbol by modul length alphabet
      newsymbol = alp[newindex] # new symbol
      ret+=newsymbol
ret = str(k) + ' '+ ret # return ready line with caption of shift
```

Simple it

```

def crypting(alp, crypt, k, ret = ''):
     return str(k_and_f)+' '+''.join([alp[(alp.index(crypt[i])+k_and_f) % len(alp)] for i in range(len(crypt))])
```

## decoding

Decoding done by analogy, but we check all shifts and need filter for bad variants

###Details

```
... # our variables
filter = ['bc', 'cd'] #bad variants

for k in range(1, len(alp): #check for all shifts
      ...
      # our coding function with repalce:
      newindex = (index - k) % 4 # index of shifted symbol by modul length alphabet # let's do it in reverse order
      ...
```
Lets make a function for check bad variants. Values:

* tmp - str, our string for check
* filter - list, our list of bad variants
* ret - Bool, return True if bad exists, else False 

```
def exists(tmp, filter, ret = True):
      for item in filter:
           if tmp.count(item) != 0 ret = False # if tmp not exists one of bad variants
      return ret
```

Let's continue:

```
filter = ['bc', 'cd'] #bad variants

for k in range(1, len(alp): #check for all shifts
      ...
      # our coding function
      ...
      if exists(ret, filter):
           ret += '\n'+str(k) + ' '+ ret # add ready line with caption of shift in ret str
```

Simple it:

```
def decrypting(alp, crypt, filter, ret = ''):
     for k in range(1,len(alp)):
          tmp = [alp[(alp.index(crypt[i])-k % 32)] for i in range(len(crypt))]
          ret += str(k)+' '+''.join(tmp)+'\n' if exists(''.join(tmp), k_and_f) else ''
     return ret
```

Let's combine functions with a variable target:

```
def crypting(target, alp, crypt, k_and_f, ret = ''):
    if target == 'encode': return str(k_and_f)+' '+''.join([alp[(alp.index(crypt[i])+k_and_f) % 32] for i in range(len(crypt))])
    else:
        for k in range(1,len(alp)):
            tmp = [alp[(alp.index(crypt[i])-k % 32)] for i in range(len(crypt))]
            ret += str(k)+' '+''.join(tmp)+'\n' if exists(''.join(tmp), k_and_f) else ''
        return ret
```

# Ready
