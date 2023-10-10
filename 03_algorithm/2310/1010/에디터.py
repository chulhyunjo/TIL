import sys
input = sys.stdin.readline

stack = list(input().rstrip())
stack2 = []
for _ in range(int(input())):
    C = input().rstrip()
    if C[0] == 'L':
        if stack:
            stack2.append(stack.pop())
    elif C[0] == 'D':
        if stack2:
            stack.append(stack2.pop())
    elif C[0] == 'B':
        if stack:
            stack.pop()
    else:
        stack.append(C[2])

stack += stack2[::-1]
print(''.join(stack))