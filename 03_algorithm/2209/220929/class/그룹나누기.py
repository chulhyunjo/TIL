def find_set(x):
    while x != tree[x]:
        x = tree[x]
    return x

def union(x, y):
    tree[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    n, m =map(int,input().split())
    pick = list(map(int,input().split()))
    tree = [i for i in range(n+1)]

    for i in range(m):
        p1, p2 = pick[i*2], pick[i*2+1]
        union(p1,p2)

    result = 0
    for num in range(1, n+1):
        if tree[num] == num:
            result += 1
    print(f'#{tc} {result}')
