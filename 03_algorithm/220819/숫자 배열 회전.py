def spin(array):
    spin_array = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            spin_array[j][n-i-1] = array[i][j]

    return spin_array


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    spin_arr1 = spin(arr)
    spin_arr2 = spin(spin_arr1)
    spin_arr3 = spin(spin_arr2)

    result_arr = [[0]*n  for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                

    print(result_arr)