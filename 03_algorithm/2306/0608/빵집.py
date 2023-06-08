import sys
input = sys.stdin.readline
dx = [-1, 0, 1]
def dfs(x, y):
    if y == C-1:
        return True
    for m in range(3):
        ax = x + dx[m]
        ay = y + 1
        if 0 <= ax < R and 0 <= ay < C:
            if graph[ax][ay] != "x" and visited[ax][ay] == -1:
                visited[ax][ay] = 1
                if dfs(ax, ay):
                    return True
    return False


R, C = map(int,input().split())
visited = [[-1]*C for _ in range(R)]
graph = [list(input().strip()) for _ in range(R)]
answer = 0

for i in range(R):
    if dfs(i, 0):
        answer += 1
print(answer)