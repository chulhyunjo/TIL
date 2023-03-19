import sys
input = sys.stdin.readline
n, k = map(int,input().split())

coin = [int(input().rstrip()) for _ in range(n)]
result = 0

for i in range(n-1, -1, -1):
    result += k //coin[i]
    k %= coin[i]

print(result)