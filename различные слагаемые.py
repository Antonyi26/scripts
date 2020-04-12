n = int(input())

k = 1

while 2*n >= k*(k+1):
	k += 1
k -= 1

N = k*(k+1) // 2
# генерируем массив значений
arr = list(range(1, k+1+1))

arr.pop(N-n-1)
print(len(arr))
print(" ".join(map(str, arr)))

