for tc in range(int(input())):
    array = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    colarr = array
    rowarr = [[array[i][j] for i in range(9)] for j in range(9)]
    squarearr = [[array[j//3 * 3 + i % 3][i//3 + j % 3 * 3] for i in range(9)] for j in range(9)]

    for col, row, square in zip(colarr, rowarr, squarearr):
        if len(set(col)) == len(set(row)) == len(set(square)):
            continue
        else:
            result = 0
            break
    print(f'#{tc+1} {result}')