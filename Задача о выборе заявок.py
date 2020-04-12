n = 10
l = [1, 0, 4, 18, 2, 5, 1, 1, 2, 7]
r = [7, 14, 9, 19, 4, 6, 7, 11, 15, 16]

a = [(r[i], l[i]) for i in range(n)]
a.sort()

cnt = 1
last_r = a[0][0]

for i in range(1, n):
    r_i, l_i = a[i]
    
    if l_i >= last_r:
        cnt += 1
        last_r = r_i
        
print(cnt)