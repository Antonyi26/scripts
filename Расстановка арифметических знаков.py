"""
Даны n чисел a1,a2,…,an.
Расставьте между ними плюсы ‘+’ и минусы ‘-’,
чтобы значение полученного выражения было равно x.
Входные данные:
В первой строке заданы два целых числа - n и x.
Во второй строке содержатся целые положительные числа a1,a2,…,an.
Выходные данные:
Выведите арифметическое выражение, значение которого равно x. Числа в выражении должны идти в том же порядке, что и во входном файле. Необходимо использовать все числа. Между каждой парой чисел  должен быть знак ‘+’ или ‘-’. Минус перед первым числом ставить нельзя.
Пример входных данных
3 0
1 2 3
Пример выходных данных
1+2-3
"""
def exp(a, sum_a, d):
    d[0][sum_a+a[0]] = 1

    for i in range(1, len(a)):
        for j in range(sum_a*2+1):

            if j+a[i] < sum_a*2:    
                if d[i-1][j+a[i]]:
                    d[i][j] = -1
            if j-a[i] >= 0:        
                if d[i-1][j-a[i]]:
                    d[i][j] = 1
############################################################
a = []
with open(r'C:\Users\Anton\Downloads\arithm2.in', 'r') as f:
    a = f.readlines()
n, target = [int(x) for x in a[0].split(' ')]
a = [int(x) for x in a[1].split(' ')]
#n = 3
#a = [1, 2, 3]
sum_a = sum(a)
#target = 0
d = [[0]*(sum_a*2+1) for i in a]

exp(a, sum_a, d)

res = []
i = len(a) - 1
j = target + sum_a
while i >= 0:
    res.insert(0, a[i] * d[i][j])
    j = j - a[i] * d[i][j]
    i -= 1

# вывод результата
print(str(res[0]), end='')
for i in range(1, len(res)):
    if res[i] > 0:
        print('+' + str(res[i]), end='')
    else:
        print(str(res[i]), end='')
print()

# вывод результата
#for i in range(n):
#    for j in range(sum_a*2+1):
#        print(d[i][j], end=' ')
#    print('')
