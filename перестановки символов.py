def rec(ind, last_sym):
    global cnt, stars, m
    
    if ind == n:
        if stars == m:
            # if cnt == 24008:
            print(str(cnt), ''.join([str(i) for i in a]))
            cnt += 1
        return
        
    for i in sym:
        if i == '*' and last_sym == '*':
            continue
        a[ind] = i
        if i == '*': stars += 1
        rec(ind+1, i)
        if i == '*': stars -= 1
        
n, m = [int(i) for i in input().split(' ')]
a = [0 for i in range(n)]
sym = ['*', '.']
# b = [False for i in range(n+1)]
cnt = 1
stars = 0
rec(0, '.')
