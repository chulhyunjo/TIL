import sys
input = sys.stdin.readline

N, M = map(int,input().split())

names = dict()
idx = []
for _ in range(N):
    name, num = input().split()
    idx.append(name)
    names[name] = int(num)

for _ in range(M):
    num = int(input())
    p = -1
    for j in range(N):
        if p < num <= names[idx[j]]:
            print(idx[j])
            break
        else:
            p = names[idx[j]]