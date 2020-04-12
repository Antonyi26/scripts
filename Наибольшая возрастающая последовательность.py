#buf = []
#with open(r'/home/antonyi/Загрузки/lis.in', 'r') as f:
# buf = f.readlines()
#n = int(buf[0])
#a = [int(x) for x in buf[1].split(' ')]
#d = [s+1 for x in range(s+1)]
#d[0] = 0
#for i in range(1, rows+1):
# a.append( [int(x) for x in buf[i].split(' ')] )
n = 5
a = [7, 1, 3, 2, 4]
d = [1 for x in range(n)]
c = [1 for x in range(n)]

ans = 0
cnt = 0
for i in range(1, n):
  ok = False
  for j in range(i):
    if a[j] < a[i]:
      if d[j] + 1 > d[i]:
        d[i] = d[j] + 1
        c[i] = c[j]
      elif d[j] + 1 == d[i]:
        c[i] += c[j]
  
  if d[i] > ans:
    ans = d[i]
    cnt = c[i]
  elif d[i] == ans:
    cnt += c[i]
  
print(ans, cnt)
  
# Выводим результат 
#for i in range(rows):
# for j in range(cols):
#   print(p[i][j], end=' ')
# print('')
