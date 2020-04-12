buf = []
with open(r'/home/antonyi/Загрузки/rucksack.in', 'r') as f:
	buf = f.readlines()
n, _W = [int(x) for x in buf[0].split(' ')]
w = []
c = []
for i in range(1, n+1):
	weight, cost = [int(x) for x in buf[i].split(' ')]
	w.append(weight)
	c.append(cost)
#a = [int(x) for x in buf[1].split(' ')]
#d = [s+1 for x in range(s+1)]
#d[0] = 0

#n = 3
#_W = 12
#w = [2, 5, 10]
#c = [10, 20, 30]
d = [[0 for y in range(_W+1)] for x in range(n+1)]

for i in range(1, n+1):
	for j in range(1, _W+1):
		if j-w[i-1] >= 0:
			if d[i-1][j-w[i-1]] + c[i-1] > d[i-1][j]:
				d[i][j] = d[i-1][j-w[i-1]] + c[i-1]
			else:
				d[i][j] = d[i-1][j]
		else:
			d[i][j] = d[i-1][j]
# определим предметы в рюкзаке
res = []
i = n
j = _W
while d[i][j] != 0:
	if d[i-1][j] == d[i][j]:
		i -= 1
	else:
		res.append(i)
		i -= 1
		j -= w[i]
	
		
print(d[n][_W])

print( ' '.join(str(x) for x in list(reversed(res))) )

# Выводим результат	
#for i in range(n+1):
#	for j in range(_W+1):
#		print(d[i][j], end=' ')
#	print('')
