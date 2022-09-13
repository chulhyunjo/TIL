def spin(ar):
    new_ar = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            new_ar[i][j] = ar[100-j-1][i]
    return new_ar


for _ in range(10):
    tc = int(input())
    array = [list(input()) for _ in range(100)]
    new_array = spin(array)
    result = 0
    max_word = 0
    for i in range(100):
        for j in range(100):
            for k in range(100-j,0,-1):
                if array[i][j:j+k] == list(reversed(array[i][j:j+k])):
                    max_word = k
                    break
                if new_array[i][j:j+k] == list(reversed(new_array[i][j:j+k])):
                    max_word = k
                    break
            result = max(result, max_word)
    print(f'#{tc} {result}')
