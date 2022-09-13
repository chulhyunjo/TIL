def spin(array):
    spin_array = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            spin_array[j][n-i-1] = array[i][j]

    return spin_array


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    spin_arr = []
    for i in range(3):
        arr = spin(arr)
        spin_arr.append(arr)
    print(f'#{tc}')
    for i in range(n):
        for j in range(3):
            for k in spin_arr[j][i]:
                print(k,end='')
            print('', end = ' ')
        print()