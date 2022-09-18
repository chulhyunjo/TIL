import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def tree_search(now,p,find1,find2):
    global cnt, result2
    if now == find1 or now == find2:
        cnt += 1
    if cnt == 2:
        result2 = p
        cnt = 0
        return

    for c in tree[now]:
        tree_search(c,p,find1,find2)

def roots(now, ch, find1, find2):
    global result
    if now == find1 or now == find2:
        result = ch
        return
    for c in tree[now]:
        roots(c,ch+[c],find1,find2)


T = int(input())
for _ in range(T):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    par = [0] * (N+1)
    for _ in range(N-1):
        a,b = map(int,input().rstrip().split())
        tree[a].append(b)
        par[b] = a

    for i in range(1,N+1):
        if par[i] == 0:
            root = i
            break
    result2 = 0
    result = []
    cnt = 0
    f1, f2 = map(int,input().split())

    roots(i,[i],f1, f2)
    for q in result:
        cnt = 0
        tree_search(q,q,f1,f2)
    print(result2)
