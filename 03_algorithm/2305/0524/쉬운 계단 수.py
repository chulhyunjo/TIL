N = int(input())
graph = [[0] * 12 for _ in range(N)]

for i in range(2,11):
    graph[0][i] = 1

for i in range(N-1):
    for j in range(1,11):
        graph[i+1][j-1] += graph[i][j]
        graph[i+1][j+1] += graph[i][j]

print(sum(graph[-1][1:11])%1000000000)
