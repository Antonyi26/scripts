# ========================================
def GetPrimeDiv(n):
    i = 1
    
    while i <= n:
        # print('IsPrime({0}) ='.format(i), IsPrime(i))
        if IsPrime(i):
            if n % i == 0:
                return i
        i += 1
        
    return 0
# ========================================
def IsPrime(n):
    if n == 1: 
        return False
    
    i = 2
    
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True
# ========================================

n = int(input('Число: '))
res = []

while n > 1:
    d = GetPrimeDiv(n)
    if not d:
        break
    res.append(d)
    n = n // d

print(' '.join([str(i) for i in res]))
