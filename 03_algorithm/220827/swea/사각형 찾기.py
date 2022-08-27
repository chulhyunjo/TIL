for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    dx = [0,1]
    dy = [1,0]
    result = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                w = h = 1
                while i + h < n and arr[i+h][j] == 1:
                    h += 1
                while j + w < n and arr[i][j+w] == 1:
                    w += 1

                for q in range(h):
                    for p in range(w):
                        arr[i+q][j+p] = 0

                result = max(result, h * w)

    print(f'#{tc} {result}')