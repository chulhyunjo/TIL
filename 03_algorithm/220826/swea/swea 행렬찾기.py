for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                w = h = 1
                while j+w < n and arr[i][j+w] > 0:
                    w += 1
                while i+h < n and arr[i+h][j] > 0:
                    h += 1

                for q in range(h):
                    for p in range(w):
                        arr[i+q][j+p] = 0

                result.append([h,w])
    result.sort(key = lambda x: x[0])
    result.sort(key = lambda x: x[0] * x[1])
    print(f'#{tc} {len(result)}', end = ' ')
    for i in result:
        print(*i, end = ' ')
    print()