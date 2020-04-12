def rec(ind, balance):
    global cnt
    
    if ind == n:
        if balance == 0:
            # if cnt == 8644:
            print(str(cnt)+'.', ''.join(a))
            cnt += 1
        return
        
    a[ind] = '('
    rec(ind+1, balance+1)
    
    if balance == 0:
        return
    
    a[ind] = ')'
    rec(ind+1, balance-1)
        
# n, m = [int(i) for i in input().split(' ')]
n = int(input())
n = 2*n
a = [0 for i in range(n)]
# b = [False for i in range(n+1)]
cnt = 1
rec(0, 0)
