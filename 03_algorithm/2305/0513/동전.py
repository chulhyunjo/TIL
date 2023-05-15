for _ in range(int(input())):
    n = int(input())
    coins = list(map(int,input().split()))
    make = int(input())
    dp = [0] * (make+1)
    dp[0] = 1
    for i in coins:
        for j in range(i, make+1):
            dp[j] = dp[j - i] + dp[j]

    print(dp[-1])