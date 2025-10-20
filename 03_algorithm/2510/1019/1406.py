import sys

input = sys.stdin.readline

stack = list(input().rstrip())
stack2 = []

M = int(input())
cursor = len(stack)

for _ in range(M):
    command = input().rstrip()

    if command[0] == "L":
        if stack:
            stack2.append(stack.pop())
    elif command[0] == "D":
        if stack2:
            stack.append(stack2.pop())
    elif command[0] == "B":
        if stack:
            stack.pop()
    elif command[0] == "P":
        stack.append(command[2])

print("".join(stack + stack2[::-1]))