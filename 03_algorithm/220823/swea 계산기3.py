for tc in range(1,11):
    n = int(input())
    math = input()
    back = ''
    stack = []

    for i in math:
        if i == ')':
            while stack[-1] != '(':
                back += stack.pop()
            stack.pop()
        elif i == '(':
            stack.append(i)
        elif i.isnumeric():
            back += i

        elif i == '+':
            if stack[-1] == '*':
                while stack and stack[-1] == '*':
                    back += stack.pop()
            if stack[-1] == '+':
                back += i
            else:
                stack.append(i)
        else:
            stack.append(i)

    idx = 0
    while idx < len(back):
        if back[idx].isnumeric():
            stack.append(int(back[idx]))

        elif back[idx] == '*':
            b, a = stack.pop(), stack.pop()
            stack.append(b*a)

        else:
            b, a = stack.pop(), stack.pop()
            stack.append(b+a)
        idx += 1
    print(f'#{tc} {stack[0]}')