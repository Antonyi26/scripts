def rec(ind):
    global cnt, n, m, a
    
    if ind == n:
        print(str(cnt)+'.', ''.join([str(i) for i in a]))
        cnt += 1
        return
    
    for i in range(1, m+1):
        a[ind] = i
        rec(ind+1)
        
n, m = [int(x) for x in input('Введите n m: ').split(' ')]
a = [0 for i in range(n)]
cnt = 1
rec(0)
