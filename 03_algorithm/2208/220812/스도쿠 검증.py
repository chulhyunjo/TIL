for tc in range(1, int(input())+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    row_arr = [[0]*9 for _ in range(9)]
    squ_arr = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            row_arr[i][j] = arr[j][i]

    for i in range(9):
        for j in range(9):
            squ_arr[i][j] = arr[3 *(i%3) + j // 3][3*(i // 3) + j % 3]

    result = 1
    for i in range(9):
        col = 0
        row = 0
        square = 0
        for j in range(9):
            col += arr[i][j]
            row += row_arr[i][j]
            square += squ_arr[i][j]

        if not col == row == square:
            result = 0
            break

    print(f'#{tc} {result}')