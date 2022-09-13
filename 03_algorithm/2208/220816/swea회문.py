def spin(array):
    spin_array = [[0] * len(array) for i in range(len(array))]
    for i in range(len(array)):
        for j in range(len(array)):
            spin_array[j][len(array)-1-i] = array[i][j]
    return spin_array

for tc in range(1, int(input())+ 1):
    result = ''
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n - m + 1):
            if arr[i][j:j+m] == list(reversed(arr[i][j:j+m])):
                result = arr[i][j:j+m]
    arr = spin(arr)
    for i in range(n):
        for j in range(n - m + 1):
            if arr[i][j:j+m] == list(reversed(arr[i][j:j+m])):
                result = arr[i][j:j+m]

    print(f'#{tc} {"".join(result)}')