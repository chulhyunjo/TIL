import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = INF
house1 = 0
house2 = 0

for i in range(1, n):
    for j in range(i+1, n+1):
        sum1 = 0
        for k in range(1,n+1):
            sum1 += min(graph[k][i], graph[k][j]) * 2
            if sum1 >= answer:
                break
        else:
            if answer > sum1:
                answer = sum1
                house1 = i
                house2 = j
print(house1, house2, answer)