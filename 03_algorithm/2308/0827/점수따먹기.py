N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
sum1 = [[0] * M for _ in range(N)]
sum1[0][0] = board[0][0]

for i in range(1, N):
    sum1[i][0] = board[i][0] + sum1[i-1][0]

for i in range(1, M):
    sum1[0][i] = board[0][i] + sum1[0][i-1]

for i in range(1, N):
    for j in range(1,M):
        sum1[i][j] = sum1[i-1][j] + sum1[i][j-1] - sum1[i-1][j-1] + board[i][j]

answer = max(map(max, sum1))

for i in range(N-1, 0, -1):
    for j in range(M-1, 0, -1):
        sum2 = sum1[i][j] - sum1[i-1][j] - sum1[i][j-1] + sum1[i-1][j-1]
        answer = max(sum2, answer)

print(answer)