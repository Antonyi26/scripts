def rec(ind):
    global cnt, n, a, used
    
    if ind == n:
        print(str(cnt)+'.', ''.join([str(i) for i in a]))
        cnt += 1
        return
    
    for i in range(1, n+1):
        
        if used[i]:
            continue
        
        a[ind] = i
        used[i] = True
        rec(ind+1)
        used[i] = False
        
n = int( input('Введите n: ') )
a = [0 for i in range(n)]
used = [False for i in range(n+1)]
cnt = 1
rec(0)
