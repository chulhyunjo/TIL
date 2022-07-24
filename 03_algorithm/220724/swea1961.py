for tc in range(int(input())):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    spin_array = []
    def spin(arr):
        spin_arr = [[0] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                spin_arr[y][n-1-x] = arr[x][y]
        return spin_arr

    for i in range(3):
        array = spin(array)
        spin_array.append(array)
    print(f'#{tc+1}')
    for i in range(n):
        for j in range(3):
            for k in spin_array[j][i]:
                print(k, end = '')
            print('', end = ' ')
        print()