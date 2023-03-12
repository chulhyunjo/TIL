import sys
input = sys.stdin.readline
weight, n = map(int, input().rstrip().split())
bag = [list(map(int, input().rstrip().split())) for _ in range(n)]
cnt = [0] * 10001
for i in range(n):
    cnt[bag[i][1]] += bag[i][0]

result = 0
for i in range(10000, 0, -1):
    if weight <= cnt[i]:
        result += weight * i
        break
    result += i * cnt[i]
    weight -= cnt[i]

print(result)