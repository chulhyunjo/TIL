from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def fire2():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]
            if 0<= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    fire.append((nx,ny))


for tc in range(int(input())):
    m, n = map(int,input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    sangen = deque()
    fire = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                sangen.append((i,j,0))
            if graph[i][j] == '*':
                fire.append((i,j))
    result = 0
    while True:
        fire2()
        for _ in range(len(sangen)):
            x, y, cnt = sangen.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
                    graph[nx][ny] = '@'
                    sangen.append((nx, ny, cnt+1))

                if 0> nx or n <= nx or 0 > ny or m <= ny:
                    result = cnt + 1
                    break
        if result or not sangen:
            break
    if result:
        print(result)
    else:
        print('IMPOSSIBLE')