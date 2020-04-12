def seq(a, b):
    d = [[0] * (len(b)+1) for i in range(len(a)+1)]

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i][j-1], d[i-1][j])
    return d[-1][-1]
############################################################
a = []
with open(r'C:\Users\Anton\Downloads\seq2.in', 'r') as f:
    a = f.readlines()
b = [int(x) for x in a[3].split(' ')]
a = [int(x) for x in a[1].split(' ')]
#a = [3, 2, 4, 2, 1, 7, 6]
#b = [4, 2, 5, 3, 1, 6, 5, 2, 3]

print(seq(a, b))
