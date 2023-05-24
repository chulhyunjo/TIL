N = int(input())
colors = list(map(int,input().split()))
K = int(input())
total = sum(colors)

DP = [[0] * (total+1) for _ in range(total+1)]

for i in range(1, total+1):
    DP[i][i] = 1
    DP[i][1] = i
    DP[i][0] = 1

for i in range(2, total+1):
    for j in range(1, i):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-1]

sum1 = 0
for color in colors:
    sum1 += DP[color][K]

print(sum1/DP[total][K])