n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

graph.sort(key = lambda x : x[0])

dp = [1] * n

for i in range(n):
    for j in range(i):
        if graph[i][1] > graph[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))