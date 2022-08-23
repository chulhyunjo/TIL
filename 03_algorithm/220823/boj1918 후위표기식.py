n = '(' + input() + ')'
result = ''
stack = []
for i in n:
    if i == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()

    elif i == '(':
        stack.append(i)

    elif i in ['-', '+']:
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(i)

    elif i in ['/', '*']:
        while stack and stack[-1] in ['*', '/']:
            result += stack.pop()
        stack.append(i)

    else:
        result += i

print(result)