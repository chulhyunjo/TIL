for tc in range(1, int(input())+1):
    n, num = input().split()
    result = ''
    for i in range(int(n)):
        a = 8
        change = num[i]
        now = ''
        if change.isnumeric(): change = int(change)
        else: change = ord(num[i]) - 55
        while a:
            now = str(change%2) + now
            a //= 2
            change //= 2
        result += now
    print(f'#{tc} {result}')