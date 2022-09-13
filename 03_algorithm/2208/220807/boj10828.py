import sys

stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack):
            x = stack.pop()
            print(x)
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)

    elif command[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
