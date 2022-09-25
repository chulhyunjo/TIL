import sys
input = sys.stdin.readline
n, p = map(int,input().split())
guitar = [[] for _ in range(7)]
result = 0

for _ in range(n):
    line, fillet = map(int,input().rstrip().split())
    while guitar[line] and guitar[line][-1] > fillet:
        guitar[line].pop()
        result += 1
    if guitar[line] and guitar[line][-1] == fillet:
        continue
    guitar[line].append(fillet)
    result += 1
print(result)
