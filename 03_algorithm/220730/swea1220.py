def spin(ar):
    new_ar = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            new_ar[i][j] = ar[100-j-1][i]
    return new_ar


for tc in range(1,11):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(n)]
    new_array = spin(array)

    for i in range(100):
        for j in range(100):
            if new_array[i][j] == 1:
                new_array[i][j] = 0
            if new_array[i][j] == 2:
                break

        for k in range(100):
            if new_array[i][99-k] == 2:
                new_array[i][99-k] = 0
            if new_array[i][99-k] == 1:
                break

    cnt = 0
    for col in new_array:
        N = 1
        for j in range(100):
            if N == 1 and col[j] == 2:
                N = 2
                cnt += 1
            if N == 2 and col[j] == 1:
                N = 1
    print(f'#{tc} {cnt}')

