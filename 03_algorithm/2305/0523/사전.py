N, M, K = map(int,input().split())

DP = [[0] * (N+M+1) for _ in range(N+M+1)]

for i in range(N+M+1):
    DP[i][i] = 1
    DP[i][0] = 1
    DP[i][1] = i

for i in range(2,N+M+1):
    for j in range(1,i):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-1]

if DP[N+M][M] < K : print(-1)
else:
    answer = [''] * (N+M)
    for i in range(N+M):
        if K > DP[N+M-1][M]:
            K -= DP[N+M-1][M]
            answer[i] = 'z'
            M -= 1
        else:
            answer[i] = 'a'
            N -= 1

    print(*answer, sep='')