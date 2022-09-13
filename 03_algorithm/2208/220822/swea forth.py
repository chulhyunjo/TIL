for tc in range(1, int(input()) + 1):
    math = input().split()
    stack = []
    op = ['+', '-', '*', '/']
    result = 0
    for i in math:
        if i == '.':
            result = stack.pop()
            break
        elif i not in op:
            stack.append(int(i))
        else:
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(b + a)
                if i == '-':
                    stack.append(b - a)
                if i == '/':
                    stack.append(b // a)
                if i == '*':
                    stack.append(b * a)
            else:
                result = 'error'
                break
    if stack:
        result = 'error'
    print(f'#{tc} {result}')
