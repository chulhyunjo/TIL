import sys
sys.setrecursionlimit(10**6)
graph = [list(map(str,input().split())) for _ in range(5)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x,y,word1):
    if len(word1) >= 6:
        result.add(word1)
        return
    word1 += graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx,ny,word1)


word = ''
result = set()
for i in range(5):
    for j in range(5):
        dfs(i,j,word)
print(result)