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

def backtracking(x, idx):
    global minV
    if minV <= x: return
    if dfs():
        minV = min(minV, x)
    if x == 3: return
    for i in range(idx+1, len(combination)):
        a, b = combination[i]
        graph[a][b] = 1
        backtracking(x+1, idx+1)
        graph[a][b] = 0
        backtracking(x, idx+1)
        break

n, m, h = map(int,input().split())
graph = [[0] * n for _ in range(h)]
line = [0] * n
for _ in range(m):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1
    line[b-1] += 1

odd = 0
for i in range(n):
    if line[i] % 2:
        odd += 1
if odd>3:
    print(-1)
    exit()

combination = set()
for i in range(h):
    for j in range(n-1):
        if j == 0 and graph[i][j] == graph[i][j+1] == 0:
            combination.add((i,j))
        elif j > 0 and graph[i][j-1] == graph[i][j+1] == graph[i][j] == 0:
            combination.add((i,j))
combination = list(combination)
minV = 4

backtracking(0, -1)
if minV != 4:
    print(minV)
else:
    print(-1)