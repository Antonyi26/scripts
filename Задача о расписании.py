#n = 10
#d = [2, 2, 1, 7, 5, 5, 4, 7, 7, 5]
#c = [92, 80, 66, 55, 55, 38, 35, 19, 16, 2]
b = []
with open(r'/home/antonyi/Загрузки/schedule2.in', 'r' ) as f:
	b = f.readlines()
n = int(b[0])
a = []
for i in range(1, n+1):
	d, c = [int(x) for x in b[i].split(' ')]
	a.append( (c,d) )
# a = [(c[i], d[i]) for i in range(n)]
a.sort()
res = [0 for i in range(n+1)]

while len(a):
    c_i, d_i = a.pop()
    
    while res[d_i]:
        d_i -= 1
        
        if d_i < 1: 
            break
    
    if d_i >= 1:
        res[d_i] = c_i
      
print(sum(res))