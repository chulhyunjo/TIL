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

def backtracking(x, idx, depth):
    global minV
    if x == depth:
        if dfs():
            print(depth)
            exit()
    else:
        if idx < l:
            a, b = combination[idx]
            graph[a][b] = 1
            backtracking(x+1, idx+1, depth)
            graph[a][b] = 0
            backtracking(x, idx+1, depth)

n, m, h = map(int,input().split())
graph = [[0] * n for _ in range(h)]
line = [0] * n
for _ in range(m):
    a, b = map(int,input().rstrip().split())
    graph[a-1][b-1] = 1
    line[b-1] += 1

odd = 0
for i in range(n):
    if line[i] % 2:
        odd += 1
if odd>3:
    print(-1)
    exit()

combination = []
l = 0
for i in range(h):
    for j in range(n-1):
        if j == 0 and graph[i][j] == graph[i][j+1] == 0:
            combination.append((i,j))
            l+=1
        elif j > 0 and graph[i][j-1] == graph[i][j+1] == graph[i][j] == 0:
            combination.append((i,j))
            l+=1

for i in range(4):
    backtracking(0, 0, i)
print(-1)