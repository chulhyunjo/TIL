import sys
input = sys.stdin.readline

N = int(input())
height = []
max_height = 0
board = [0] * 1002
for _ in range(N):
    x, h = map(int,input().split())
    board[x] = h
    height.append((x,h))

height.sort()
max_height = max(board)
h = 0
idx = height[0][0]
answer = max_height
for i in range(N):
    if h <= height[i][1]:
        answer += h * (height[i][0] - idx)
        idx = height[i][0]
        if height[i][1] == max_height:
            max_height = max(board[height[i][0]+1:])
            h = max_height
        else:
            h = height[i][1]


print(answer)