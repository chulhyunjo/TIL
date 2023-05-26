import sys
input = sys.stdin.readline

while True:
    maxV = 0
    stack = []
    n, *heights = map(int,input().split())
    if n == 0: break
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