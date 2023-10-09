N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dp = [[[1000,1000,1000] for _ in range(M)] for _ in range(N)]

for i in range(M):
    dp[0][i] = [graph[0][i],graph[0][i],graph[0][i]]

for i in range(1, N):
    for j in range(M):
        if j == 0:
            dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][0]+graph[i][j], dp[i-1][j][2]+graph[i][j])
            dp[i][j][2] = min(dp[i][j][2], dp[i-1][j+1][1] + graph[i][j], dp[i-1][j+1][0]+graph[i][j])
        elif j == M-1:
            dp[i][j][0] = min(dp[i][j][0], dp[i-1][j-1][1]+graph[i][j], dp[i-1][j-1][2] + graph[i][j])
            dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][0]+graph[i][j], dp[i-1][j][2]+graph[i][j])
        else:
            dp[i][j][0] = min(dp[i][j][0], dp[i - 1][j - 1][1] + graph[i][j], dp[i - 1][j - 1][2] + graph[i][j])
            dp[i][j][1] = min(dp[i][j][1], dp[i - 1][j][0] + graph[i][j], dp[i - 1][j][2]+graph[i][j])
            dp[i][j][2] = min(dp[i][j][2], dp[i - 1][j + 1][1] + graph[i][j], dp[i - 1][j + 1][0] + graph[i][j])

answer = 1000
for i in range(M):
    answer = min(answer, min(dp[N-1][i]))
print(answer)