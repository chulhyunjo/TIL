from pprint import pprint
n = int(input())
graph = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y, y+10):
            graph[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
area = 0
for i in range(1,101):
    for j in range(1,101):
        if graph[i][j] == 1:
            cnt = 0
            for q in range(4):
                nx = i + dx[q]
                ny = j + dy[q]

                if 0 <= nx < 101 and 0 < ny < 101:
                    if graph[nx][ny] == 1:
                        cnt += 1

            area += (4 - cnt)
print(area)