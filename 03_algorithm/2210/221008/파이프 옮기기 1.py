import sys
sys.setrecursionlimit(10**6)
# status: 1 가로, 2 세로, 3 대각선
def find(x, y, status):
    global result
    if x == n-1 and y == n-1:
        result += 1
        return

    if status != 2:
        if y + 1 < n and graph[x][y+1] == 0:
            find(x, y+1, 1)

    if status != 1:
        if x + 1 < n and graph[x+1][y] == 0:
            find(x+1, y, 2)

    if x + 1 < n and y + 1 < n and graph[x+1][y] == graph[x][y+1] == graph[x+1][y+1] == 0:
        find(x+1, y+1, 3)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result = 0
find(0, 1, 1)
print(result)