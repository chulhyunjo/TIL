def spin(ar):
    new_ar = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            new_ar[i][j] = ar[8-j-1][i]
    return new_ar


for tc in range(1,11):
    n = int(input())
    array = [list(input()) for _ in range(8)]
    cnt = 0
    new_array = spin(array)

    for i in range(8):
        for j in range(8-n+1):
            if array[i][j:j+n] == list(reversed(array[i][j:j+n])):
                cnt += 1
            if new_array[i][j:j+n] == list(reversed(new_array[i][j:j+n])):
                cnt += 1
    print(f'{tc} {cnt}')

