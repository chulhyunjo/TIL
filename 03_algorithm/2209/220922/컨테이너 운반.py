for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    w = sorted(list(map(int,input().split())))
    truck = sorted(list(map(int,input().split())))
    visited = [0] * n
    result = 0
    for i in range(m):
        move_idx = -1
        for j in range(n):
            if w[j] <= truck[i] and not visited[j]:
                move_idx = j
            if w[j] > truck[i]:
                break
        if move_idx != -1:
            result += w[move_idx]
            visited[move_idx] = 1

    print(f'#{tc} {result}')