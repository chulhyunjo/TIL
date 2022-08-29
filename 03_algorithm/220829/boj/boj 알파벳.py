import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y,cnt):
    global max_cnt
    max_cnt = max(max_cnt,cnt)
    alpha[arr[x][y]] = 1
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < m:
            if alpha[arr[nx][ny]] == 0:
                dfs(nx,ny,cnt +1)
                alpha[arr[nx][ny]] = 0


n, m = map(int,input().split())
arr = [list(map(lambda x: ord(x) - 65, input())) for _ in range(n)]
max_cnt = 0
alpha = [0] * 26
dfs(0,0,1)
print(max_cnt)