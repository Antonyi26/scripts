buf = []
with open(r'/home/antonyi/Загрузки/rectangle.in', 'r') as f:
	buf = f.readlines()
n, m = [int(x) for x in buf[0].split(' ')]
#a = [int(x) for x in buf[1].split(' ')]
#d = [s+1 for x in range(s+1)]
#d[0] = 0

rows = n
cols = m

a = []
for i in range(1, rows+1):
	a.append( [int(x) for x in buf[i].split(' ')] )
len_query = int(buf[rows+1])
query = []
for i in range(len_query):
	query.append( [int(x) for x in buf[i+rows+2].split(' ')] )
	
s = [[0 for x in range(cols+1)] for y in range(rows+1)]
s[1][1] = a[0][0]
# заполняем первую строку и первый столбец
for j in range(2, cols+1):
	s[1][j] = s[1][j-1] + a[0][j-1]
for i in range(2, rows+1):
	s[i][1] = s[i-1][1] + a[i-1][0]
# заполняем таблицу сумм
for i in range(2, rows+1):
	for j in range(2, cols+1):
		s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i-1][j-1]
############################################
_sum = 0
for q in query:
	x1, x2, y1, y2 = q
	_sum += s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1]

print(_sum)

# Выводим результат	
#for i in range(rows):
#	for j in range(cols):
#		print(s[i][j], end=' ')
#	print('')
