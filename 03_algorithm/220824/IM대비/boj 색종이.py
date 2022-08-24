n = int(input())
graph = [[0] * 100 for _ in range(100)] # 100 x 100도화지
for _ in range(n):
    x, y = map(int,input().split()) # 색종이 왼쪽 아래 모서리 좌표
    for i in range(x, x+10):
        for j in range(y, y+10):
            graph[i][j] = 1
cnt = 0
for i in graph:
    cnt += i.count(1)

print(cnt)