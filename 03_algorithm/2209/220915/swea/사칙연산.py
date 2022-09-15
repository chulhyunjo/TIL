def inorder(n):
    if 0 < n <= N:
        if tree[n] == '+':
            return inorder(child[n][0]) + inorder(child[n][1])

        elif tree[n] == '-':
            return inorder(child[n][0]) - inorder(child[n][1])

        elif tree[n] == '*':
            return inorder(child[n][0]) * inorder(child[n][1])

        elif tree[n] == '/':
            return inorder(child[n][0]) / inorder(child[n][1])

        else:
            return tree[n]


T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    child = [[] for _ in range(N + 1)]

    # 트리 정보 입력
    for _ in range(N):
        n, t, *c = input().split()

        tree[int(n)] = int(t) if t.isnumeric() else t
        child[int(n)] = list(map(int, c))

    result = inorder(1)
    print(f'#{tc} {int(result)}')