buf = []
with open(r'/home/antonyi/Загрузки/change.in', 'r') as f:
	buf = f.readlines()
n, s = [int(x) for x in buf[0].split(' ')]
a = [int(x) for x in buf[1].split(' ')]
d = [s+1 for x in range(s+1)]
d[0] = 0
#for i in range(1, rows+1):
#	a.append( [int(x) for x in buf[i].split(' ')] )

for i in range(s+1):
	for j in range(len(a)):
		if i - a[j] >= 0:
			d[i] = min(d[i], d[i-a[j]] + 1)

print(d[s])
# Выводим результат	
#for i in range(rows):
#	for j in range(cols):
#		print(p[i][j], end=' ')
#	print('')
