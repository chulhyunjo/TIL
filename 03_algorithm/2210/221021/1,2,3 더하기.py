dp=[0]*10
dp[0] = 1
dp[1] = 2
dp[2] = dp[0]+dp[1]+1
for i in range(3,10):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for _ in range(int(input())):
    n = int(input())
    print(dp[n-1])