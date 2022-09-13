import sys
input = sys.stdin.readline

n = int(input())
building = [int(input()) for _ in range(n)]
stack = []
result = [0] * n
for i in range(1, n):
    stack.append((building.pop(), i)) # i -> 현재 빌딩의 위치 반대순

    while stack and stack[-1][0] < building[-1]:
        stack.pop()

    if stack:
        result[i] += i - stack[-1][1]
    else:
        result[i] = i
print(sum(result))