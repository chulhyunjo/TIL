n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
INF = 10**6
dp = [[INF,INF,INF] for _ in range(n)]
dp[0][0] = graph[0][0]
dp[0][1] = graph[0][1]
dp[0][2] = graph[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + graph[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + graph[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + graph[i][2]

print(min(dp[n-1]))