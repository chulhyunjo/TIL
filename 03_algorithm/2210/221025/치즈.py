from collections import deque

def find():
    queue = deque()
    queue.append((0,0))
    v = [0] * (m*n)
    v[0] = 1
    result = set()
    while queue:
        x, y = queue.popleft()
        for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if nx<0 or ny<0 or nx>=n or ny>=m or v[nx*m + ny]: continue
            if graph[nx][ny] == 1:
                v[nx*m+ny] = 1
                result.add((nx,ny))
            if graph[nx][ny] == 0:
                v[nx*m + ny] = 1
                queue.append((nx,ny))
    return result
n, m = map(int,input().split())
graph = []
total = 0
for i in range(n):
    line = list(map(int,input().split()))
    for j in range(m):
        if line[j] == 1:
            total += 1
    graph.append(line)

cnt = 0
while total:
    cnt += 1
    cheese = find()
    tmp = total
    if cheese:
        for x, y in cheese:
            graph[x][y] = 0
            total -= 1

print(cnt, tmp, sep='\n')