word = list(input())
stack = []
cnt = 0

result = 0
while word:
    stack.append(word.pop())
    if stack[-1].isdigit():
        stack.pop()
        if stack:
            cnt += 1
        else:
            result += 1

    elif stack[-1] == '(':
        x = word.pop()
        stack.pop()
        stack.pop()
        cnt = cnt * int(x)
        if not stack:
            result += cnt
            cnt = 0

print(result)


