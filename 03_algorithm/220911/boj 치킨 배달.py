from collections import deque
from itertools import combinations
dx = [1,-1,0,0]
dy = [0,0,1,-1]
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i,j))
ans = 1000000
for i in combinations(chicken,m):
    result = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] == 1:
                tmp = 1000000
                for a,b in i:
                    distance = abs(j-a) + abs(k-b)
                    tmp = min(tmp, distance)
                result += tmp
    ans = min(result, ans)
print(ans)