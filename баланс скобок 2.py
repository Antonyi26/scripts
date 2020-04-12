def balanced(a):
    balance = []
    
    for i in range(len(a)):        
        if len(balance) == 0:
            balance.append(a[i])        
        elif balance[-1] == '(' and a[i] == ')':
            balance.pop()
        elif balance[-1] == '[' and a[i] == ']':
            balance.pop()
        else: balance.append(a[i])
    
    if len(balance) == 0:
        return True
        
    return False
# -----------------------------------------
def rec(ind):
    global n, a, cnt
    
    if ind == n:
        if balanced(a):
            # if cnt == 8644:
            print(str(cnt), ''.join(a))
            cnt += 1
        return
    
    for i in ['(', ')', '[', ']']:
        a[ind] = i
        rec(ind+1)
# -----------------------------------------    
n = int(input())
n = 2*n
a = [0 for i in range(n)]

cnt = 1
rec(0)
