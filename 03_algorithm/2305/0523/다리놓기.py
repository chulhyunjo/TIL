DP = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    DP[i][i] = 1
    DP[i][0] = 1
    DP[i][1] = i

for i in range(2,31):
    for j in range(1,i):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
        
for _ in range(int(input())):
    n, m = map(int,input().split())
    print(DP[m][n])