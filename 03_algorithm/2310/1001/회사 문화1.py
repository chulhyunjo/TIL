import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def plus(i, score):
    for nx in tree[i]:
        answer[nx] += score
        plus(nx, score)

n, m = map(int,input().split())
parents = list(map(int,input().split()))
answer = [0] * (n+1)

tree = [[] for _ in range(n+1)]
for i in range(1,n+1):
    if parents[i-1] != -1:
        tree[parents[i-1]].append(i)

give = [0] * (n+1)
for _ in range(m):
    i, w = map(int,input().split())
    give[i] += w

for i in range(n+1):
    if give[i]:
        answer[i] += give[i]
        plus(i, give[i])

print(*answer[1:])