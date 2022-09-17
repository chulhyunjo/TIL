import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def tree_search(pre,now):
    visited[now] = 0
    for i in tree[now]:
        if visited[i]:
            tree_search(now,i)
    if animal[now][0] == 'W':
        if result[now] - animal[now][1] < 0:
            result[pre] += 0
        else:
            result[pre] += result[now] - animal[now][1]
    if animal[now][0] == 'S':
        result[pre] += result[now] + animal[now][1]

N = int(input().rstrip())
tree = [[] for _ in range(N+1)]
animal = [('',0)] * (N+1)
for q in range(2,N+1):
    A, num, p = input().rstrip().split()
    tree[q].append(int(p))
    tree[int(p)].append(q)
    animal[q]=(A,int(num))
result = [0] * (N+1)
visited = [1] * (N+1)
tree_search(1,1)
print(result[1])