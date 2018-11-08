# Laboratory work №1

This is one of the classic algorithms - Cesar Algorithm.

## Principle:

Shift each symbol in line for k. 

### Example

Let alphabet = 'abcd', let line = 'abcd'

for k = 1:

| a | b | c | d | -> | b | c | d | a |
|---|---|---|---|---|---|---|---|---| 




for k = 2:

| a | b | c | d | -> | c | d | a | b |
|---|---|---|---|---|---|---|---|---|


Back by analogy

## coding

Function crypting can code and decode line. It determined by "target" variable. Function accept values:

* target - st, can be 'encode' or 'decode';
* alp - str, current alphabet for coding, decoding;
* crypt - str, line, which needs in coding or decoding;
* k_and_f - (int, list), shift if encoding, or filter of bigrams if decoding;
* ret = '' - str, initial line for return.

### Details:

```python
alp = 'abcd'
crypt = 'abcd'
k = 1 #shift
size = len(crypt) # length of crypt
alp_size = len(alp) # length of alphabet
ret = '' # answer
for i in range(size):
      symbol = crypt[i] #current symbol with shift
      index = alp.index(symbol) # index symbol in alp
      newindex = (index + k) % len(alp) # index of shifted symbol by modul length alphabet (4)
      newsymbol = alp[newindex] # new symbol
      ret+=newsymbol
ret = str(k) + ' '+ ret # return ready line with caption of shift
```

Simple it

```python
def crypting(alp, crypt, k, ret = ''):
     return str(k_and_f)+' '+''.join([alp[(alp.index(crypt[i])+k_and_f) % len(alp)] for i in range(len(crypt))])
```

## decoding

Decoding done by analogy, but we check all shifts and need filter for bad variants

### Details:

```python
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

```python
def exists(tmp, filter, ret = True):
      for item in filter:
           if tmp.count(item) != 0: ret = False # if tmp not exists one of bad variants
      return ret
```

Let's continue:

```python
filter = ['bc', 'cd'] #bad variants

for k in range(1, len(alp): #check for all shifts
      ...
      # our coding function
      ...
      if exists(ret, filter):
           ret += '\n'+str(k) + ' '+ ret # add ready line with caption of shift in ret str
```

Simple it:

```python
def decrypting(alp, crypt, filter, ret = ''):
     for k in range(1,len(alp)):
          tmp = [alp[(alp.index(crypt[i])-k % len(alp))] for i in range(len(crypt))]
          ret += str(k)+' '+''.join(tmp)+'\n' if exists(''.join(tmp), k_and_f) else ''
     return ret
```

Let's combine functions with a variable target:

```python
def crypting(target, alp, crypt, k_and_f, ret = ''):
    if target == 'encode': return str(k_and_f)+' '+''.join([alp[(alp.index(crypt[i])+k_and_f) % 32] for i in range(len(crypt))])
    else:
        for k in range(1,len(alp)):
            tmp = [alp[(alp.index(crypt[i])-k % len(alp)] for i in range(len(crypt))]
            ret += str(k)+' '+''.join(tmp)+'\n' if exists(''.join(tmp), k_and_f) else ''
        return ret
```

# Ready

# Laboratory work №2
Playfer algorithm
## Principle
We need to create a matrix, which contains key and remaining letter of alphabet.
Let alp = 'abcdefgh', key = 'bcfg' 
Then Matrix:

| | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | B | C | F | G |
| 1 | A | D | E | H |

With the matrix we coding phrase. 
## Preparing
Split phrase on pairs:
If in pair only one letter, or two same letters, we need insert substitutional letter between them
or in the end of phrase. 

Let the substitutional letter E.
### Example 1
Let we need code phrase 'BACFAAG'.
Split:
| BA | CF | AA | G |
|---|---|---|---|
We need to insert E in pair 'AA':
| BA | CF | AE | AG |
|---|---|---|---|
Good. 
### Example 2
Let we need code phrase 'BACFCAG'.
Split:
| BA | CF | CA | G |
|---|---|---|---|
We need to insert E in the end:
| BA | CF | CA | GE |
|---|---|---|---|

## Crypt

| | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | B | C | F | G |
| 1 | A | D | E | H |
Our phrase:
| BA | CF | AG |
|---|---|---|

If pair are located in one row, then we shift down for 1 and replace:
| BA | -> | AB |
|---|---|---|
If pair are located in one column, the we shift right for 1 and replace:
| CF | -> | FG |
|---|---|---|
Else we must take the letters standing at the intersection:
| AG | -> | HB |
|---|---|---|

Back for Analogy

## Coding
Function crypting can code and decode line. It determined by "target" variable. Function accept values:

* target - str, can be 'encode' or 'decode';
* alp - list, current alphabet for coding, decoding;
* keyword - list, current keyword
* crypt - str, line, which needs in coding or decoding;
* phrase - str, initial line for return.

### Details

Creating matrix of letters:
```python
def crypting(alp, keyword, crypt):
    m, n = 4,2 #size of our table
    str = keyword + alp
    newstr = ''
    for item in str:
        if not str in newstr: # if item not exist in list, append them
            newstr+=str
    table = list(newstr)
    table = np.reshape(table, (m,n)) #Create matrix of letters
```

Simple it:

```python
...
    table = np.reshape(list(OrderedDict(zip(keyword + alp, repeat(None)))), (4,2))
```

After creating table we need prepare our phrase:

```python
for i in range(0,len(crypt)-1,2): # step 2, because we need a bigrams
    if crypt[i] == crypt[i+1]:  #if neighbors are equal, insert special symbol between them
        crypt = crypt[:i+1]+'E'+crypt[i+1:]
    if len(crypt) % 2 != 0: crypt+='E' # if length of phrase odd, insert special symbol in the end
    crypt = crypt.replace(' ','') # replace spaces...
    crypt = crypt.replace('X','A') # ...and missing letters
```

Let's create function and simple it:

```python
def groupby(iterable, target):
        for i in range(0,len(iterable)-1,2):
            if iterable[i] == iterable[i+1]: iterable = iterable[:i+1]+'E'+iterable[i+1:]
        if len(iterable) % 2 != 0: iterable+='E' 
        iterable = iterable.translate(''.maketrans('X','A')).replace(' ', '')
    return zip(*([iter(iterable)] * 2)) # return list of bigrams
```

Return two our table. Let's take a list of bigrams:

```python
...
    table = np.reshape(list(OrderedDict(zip(keyword + alp, repeat(None)))), (5,6))
    crypt = [''.join(i) for i in groupby(crypt,target)]
```

Let's start coding our phrase:

```python
...
for i, j in crypt: # i and j = 'E' and 'A' if bigram was 'EA'
    #we need to get positions of elements i,j
    y1, x1 = list(map(np.asscalar, np.where(table == i)))
    y2, x2 = list(map(np.asscalar, np.where(table == j)))
    # if letters in one column
    if x1 == x2: phrase+=table[y1+1][x1]+table[y2+1][x2]
    # if letter in one row
    elif y1 == y2: phrase+=table[y1][x1+1]+table[y2][x2+1]
    # else
    else: phrase+=table[y1][x2]+table[y2][x1]
return phrase
```

Decoding by analogy in reverse order. Let's add in our functions
ability for decoding with variable target and simple it:

```python
def groupby(iterable, target):
    if target == 'encode':
        for i in range(0,len(iterable)-1,2):
            if iterable[i] == iterable[i+1]: iterable = iterable[:i+1]+'E'+iterable[i+1:]
        if len(iterable) % 2 != 0: iterable+='E' 
        iterable = iterable.translate(''.maketrans('X','A')).replace(' ', '')
    return zip(*([iter(iterable)] * 2))

def crypting(target, alp, keyword, crypt, phrase = ''):
    z, f = (4, 5) if target == 'encode' else (1, 1)
    table = np.reshape(list(OrderedDict(zip(keyword + alp, repeat(None)))), (5,6))
    crypt = [''.join(i) for i in groupby(crypt,target)]
    for i, j in crypt:
        y1, x1 = list(map(np.asscalar, np.where(table == i)))
        y2, x2 = list(map(np.asscalar, np.where(table == j)))
        if x1 == x2: phrase+=table[y1-z][x1]+table[y2-z][x2]
        elif y1 == y2: phrase+=table[y1][x1-f]+table[y2][x2-f]
        else: phrase+=table[y1][x2]+table[y2][x1]
    return phrase
```
# Ready
