def dyn(n, a):
    d = [[float('inf')]*n for x in range(1 << n)]
    d[0][0] = 0
    
    for mask in range(1 << n):
        for i in range(n):
            if d[mask][i] == float('inf'):
                continue
            for j in range(n):
                if not (mask & (1 << j)):
                    if d[mask ^ (1 << j)][j] > d[mask][i] + a[i][j]:
                        d[mask ^ (1 << j)][j] = d[mask][i] + a[i][j]
                    #d[mask ^ (1 << j)][j] = min(d[mask ^ (1 << j)][j], d[mask][i] + a[i][j])
    return d[-1][0]
###########################################################
def rec(ind):
    global n, a, rout, used, res, find
    
    if ind == n:
        s = 0
        for i in range(1, n):
            s += a[rout[i-1]][rout[i]]
        s += a[rout[-1]][0]
        if s < res[0]:
            res[0] = s
            res[1] = rout[:]
        return
    
    for i in range(n):
        
        if used[i]:
            continue
        
        rout[ind] = i
        used[i] = True
        rec(ind+1)
        used[i] = False
        
        if ind == 0 and i == 0:
            break
###########################################################
n = 0
a = []

with open(r'C:\Users\Anton\Downloads\salesman2.in', 'r') as f:
    buf = f.readlines()
    n = int(buf[0])
    for i in range(1, n+1):
        a.append( [int(x) for x in buf[i].split(' ')] )


print(dyn(n, a))

#used = [False] * n
#res = [float('inf'), None]
#rout = [0] * n
#rec(0)
#print(res)

# вывод результата
#for i in range(n):
#    for j in range(n):
#        print(str(a[i][j]).rjust(3), end=' ')
#    print('')

#print()

#for i in range(1 << n):
#    for j in range(n):
#        print(str(d[i][j]).rjust(3), end=' ')
#    print('')
