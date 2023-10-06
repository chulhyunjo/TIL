import sys
input = sys.stdin.readline

N = int(input())
names = dict()
for _ in range(N*2-1):
    name = input().rstrip()
    if names.get(name, 0):
        del names[name]
    else:
        names[name]= 1

print(*names.keys())