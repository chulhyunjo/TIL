for tc in range(int(input())):
    n = int(input())
    cnt = 1
    result = []
    while True:
        new_num = cnt * n
        for i in str(new_num):
            result.append(i)
            result = list(set(result))

        if len(result) == 10:
            break
        cnt += 1
    print(f'#{tc + 1} {new_num}')
