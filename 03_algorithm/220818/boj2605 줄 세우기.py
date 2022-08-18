n = int(input())
line = list(map(int,input().split()))
stack = []
result = []
for i in range(n):
    for j in range(line[i]):
        stack.append(result.pop())
    stack.append(i+1)
    while stack:
        result.append(stack.pop())

print(*result)