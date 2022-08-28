from itertools import combinations
from collections import deque
import copy
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

zeroArr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zeroArr.append([i,j])

result = 0
for i in combinations(zeroArr,3):
    new_graph = copy.deepcopy(graph)
    for j in i:
        new_graph[j[0]][j[1]] = 1
    queue = deque()
    for q in range(n):
        for p in range(m):
            if new_graph[q][p] == 2:
                queue.append((q,p))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
                            queue.append((nx,ny))
                            new_graph[nx][ny] = 1
    cnt = 0
    for q in new_graph:
        cnt += q.count(0)

    result = max(cnt, result)
print(result)