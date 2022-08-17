for tc in range(1, int(input())+1):
    sentence = input()
    stack = []
    result = 1
    for i in sentence:
        if i not in ['(', ')', '{', '}']:
            continue
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break

    if stack:
        result = 0
    print(f'#{tc} {result}')