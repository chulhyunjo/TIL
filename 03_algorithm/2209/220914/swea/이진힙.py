def heap(i):
    global last
    last += 1
    tree[last] = i
    c = last
    p = c//2
    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


def result(n):
    global ans
    p = n // 2
    while p:
        ans += tree[p]
        p = p // 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    last = 0
    tree = [0] * (N+1)
    for q in arr:
        heap(q)
    ans = 0
    result(N)
    print(f'#{tc} {ans}')