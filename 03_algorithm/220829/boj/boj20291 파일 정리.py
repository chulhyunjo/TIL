import sys
input = sys.stdin.readline
n = int(input())
result = dict()
for _ in range(n):
    a, b = input().rstrip().split('.')
    if b not in result:
        result[b] = 1
    else:
        result[b] += 1

for k,v in sorted(result.items()):
    print(k,v)