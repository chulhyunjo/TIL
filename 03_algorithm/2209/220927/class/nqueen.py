def n_queen(i, col):
    a = len(col) - 1
    if promising(i,col):
        if i == a:
            result.append(col[1:])
        else:
            for j in range(1,a+1):
                col[i+1] = j
                n_queen(i+1, col)


def promising(i,col):
    k = 1
    flag = True
    while k < i and flag:
        if col[k] == col[i] or abs(col[k] - col[i]) == i-k:
            flag = False
        k += 1
    return flag

for tc in range(1, int(input())+1):
    result = []
    n = int(input())
    col = [0] * (n+1)
    n_queen(0,col)
    print(f'#{tc} {len(result)}')