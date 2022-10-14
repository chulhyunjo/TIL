def check(a, b):
    if a == '>' and b == '<':
        return True
    elif a == ']' and b == '[':
        return True
    elif a == '}' and b == '{':
        return True
    elif a == ')' and b == '(':
        return True

for tc in range(1, 11):
    n = int(input())
    arr = list(input())
    stack = []
    while arr:
        stack.append(arr.pop())
        while stack and arr and check(stack[-1], arr[-1]):
            stack.pop()
            arr.pop()

    if stack:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
