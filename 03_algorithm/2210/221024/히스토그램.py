import sys
input = sys.stdin.readline
n = int(input())
maxV = 0
stack = []
heights = [int(input().rstrip()) for _ in range(n)]

for idx in range(n):
    while stack and heights[stack[-1]] > heights[idx]:
        height = heights[stack[-1]]
        width = idx
        stack.pop()
        if stack:
            width = (idx-1-stack[-1])
        area = width * height
        maxV= max(area, maxV)
    stack.append(idx)

while stack:
    height = heights[stack[-1]]
    width = n
    stack.pop()
    if stack:
        width = (n-1-stack[-1])
    area = width * height
    maxV = max(area, maxV)

print(maxV)