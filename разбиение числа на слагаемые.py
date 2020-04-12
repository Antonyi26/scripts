def rec(ind, sum, last_i):
    global cnt
    
    if sum == n:
        #if cnt <= 13672:
        print(str(cnt)+'.', '+'.join([str(i) for i in a[:ind]]))
        cnt += 1
        return
        
    for i in range(last_i, n+1):
        a[ind] = i
        if sum+i > n:
            continue
        rec(ind+1, sum+i, i)
        
n = int(input())
a = [0 for i in range(n)]
# b = [False for i in range(n+1)]
cnt = 1
rec(0, 0, 1)
