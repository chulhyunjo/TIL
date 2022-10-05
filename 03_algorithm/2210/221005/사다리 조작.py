def dfs():
    for i in range(n):
        start = i
        for j in range(h):
            if graph[j][start] and start < n-1:
                start += 1
            elif start > 0 and graph[j][start-1]:
                start -= 1
        if start != i:
            return 0
    return 1

def backtracking(x, d, e):
    global minV
    if minV <= x: return
    if dfs():
        minV = min(minV, x)
    if x == 3: return
    for i in range(d, h):
        if i == d: k = e    # 같은 줄에선 다음 곳 확인
        else: k = 0         # 줄이 바뀌면 첫 줄 부터 확인
        for j in range(k, n-1):
            if graph[i][j+1] == 1:
                continue
            if graph[i][j] == 0:
                graph[i][j] = 1
                backtracking(x+1, i, j+2)
                graph[i][j] = 0

n, m, h = map(int,input().split())
graph = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1
minV = 4

backtracking(0, 0, 0)
if minV != 4:
    print(minV)
else:
    print(-1)