for tc in range(1, int(input())+1):
    arr = []
    for i in range(5):
        line = list(input())
        while len(line) < 15:
            line.append('')
        arr.append(line)

    result = ''
    for i in range(15):
        for j in range(5):
            result += arr[j][i]
    print(f'#{tc} {result}')