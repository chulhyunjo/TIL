import sys
sys.setrecursionlimit(250000)


def bfs(i, j):
    global width
    width += 1
    paper[i][j] = 0
    for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<m and paper[ni][nj] != 0:
            bfs(ni, nj)
    return


n, m = map(int, sys.stdin.readline().rstrip().split())
paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

cnt = 0
V = []

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            cnt += 1
            width = 0
            bfs(i, j)
            V.append(width)

print(cnt)
if not V:
    print(0)
else:
    print(max(V))