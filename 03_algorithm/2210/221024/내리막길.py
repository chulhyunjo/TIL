import sys
sys.setrecursionlimit(10**5)

def dfs(x,y):
    result = 0
    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        for dx, dy in [[1,0],[-1,0], [0,1],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if nx<0 or ny<0 or n<=nx or m<=ny: continue
            if graph[nx][ny] < graph[x][y]:
                result += dfs(nx,ny)
    dp[x][y] = result
    return result

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
r = dfs(0,0)
print(r)