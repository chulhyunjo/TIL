"""
입력
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

출력
6
"""

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

result = 0
for coin in coins:
    result += K // coin
    K %= coin

print(result)