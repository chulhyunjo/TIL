import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    x = int(input().rstrip())
    if x == 0:
        s.pop()
    else:
        s.append(x)

print(sum(s))