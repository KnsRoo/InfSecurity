import randomtools as rt

def custom_hash(phrase, m):
    return sum([ord(i) for i in phrase])%m

for i in range(1000):
    print('Generating...')
    key = 'Hello, Alisa'
    p, g = rt.randomprime()
    print(p,g)
    m = custom_hash(key,p-1)
    x = rt.randedge(1,p)
    k, inv = rt.randomk(p)
    y = pow(g,x,p)
    r = pow(g,k,p)
    print('Opened key =',p,g,y)
    s = ((m-x*r)*inv) % (p-1)
    print('Closed key = <',r,',',s,'>')
    print('Checking...')
    if (0 < r < p) and (0 < s < p-1): 
        z = custom_hash(key,p-1)
        a = (pow(y,r,p)*pow(r,s,p)) % p
        b = pow(g,z,p)
        if a == b: print('Valid')
        else: 
            print('Not Valid')
            break