import sys
sys.setrecursionlimit(10 ** 6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, digit):
    if len(digit) == 6:
        result.add(digit)
        return
    digit += str(graph[x][y])
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, digit)


graph = [list(map(int, input().split())) for _ in range(5)]
result = set()
digits = ''
for i in range(5):
    for j in range(5):
        dfs(i, j, digits)
print(len(result))
