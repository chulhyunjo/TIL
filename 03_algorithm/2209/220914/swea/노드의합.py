def post(i):
    if 2 * i <= N:
        post(2*i)
        post(2*i+1)
        if tree[i] == 0:
            if 2*i+1 > N:
                tree[i] = tree[2*i]
            else:
                tree[i] = tree[2*i] + tree[2*i+1]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int,input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int,input().split())
        tree[a] = b

    post(1)
    print(f'#{tc} {tree[L]}')