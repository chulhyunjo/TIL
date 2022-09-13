def spin(array):
    spin_array = [[0] * len(array) for i in range(len(array))]
    for i in range(len(array)):
        for j in range(len(array)):
            spin_array[j][len(array)-1-i] = array[i][j]
    return spin_array

for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    result = ''
    for i in range(n):
        for j in range(n-m+1):
            check_col = arr[i][j:j+m]
            if check_col == check_col[::-1]:
                result = check_col

    arr = spin(arr)

    for i in range(n):
        for j in range(n-m+1):
            check_row = arr[i][j:j+m]
            if check_row == check_row[::-1]:
                result = check_row
    result = ''.join(result)
    print(f'#{tc} {result}')