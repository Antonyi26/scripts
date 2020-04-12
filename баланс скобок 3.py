def balanced(a):
    balance = []
    
    for i in range(len(a)):        
        if len(balance) == 0:
            balance.append(a[i])        
        elif balance[-1] == '(' and a[i] == ')':
            balance.pop()
        elif balance[-1] == '[' and a[i] == ']':
            balance.pop()
        elif balance[-1] == '{' and a[i] == '}':
            balance.pop()
        else: balance.append(a[i])
        
    return balance
# -----------------------------------------
def balancing(a):
    global mirror_bracket
    
    if type(a) == type(' '):
        a = list(a)
        
    opened_brackets = []
    closed_brackets = []
    
    balance = balanced(a)
    
    if balance == 0:
        return ''.join(a)
    
    for i in balance:
        if i in ('(','[','{'):
            opened_brackets.append(i)
        if i in (')',']','}'):
            closed_brackets.append(i)
    
    while len(opened_brackets):
        a.append( mirror_bracket[opened_brackets.pop()] )
    
    while len(closed_brackets):
        a.insert(0, mirror_bracket[closed_brackets.pop(0)] )
    
    balance = balanced(a)

    print(a)
    
    if len(balance) == 0:
        return ''.join(a)
    return 'IMPOSSIBLE'
# -----------------------------------------
mirror_bracket = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
}
test = input()    
print( balancing(test) )
    
        
