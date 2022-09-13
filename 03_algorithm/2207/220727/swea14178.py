for tc in range(1, int(input())+1):
    n, d = map(int, input().split())
    water = 2*d + 1
    if n % water == 0:
        result = n // water
    else:
        result = n // water + 1

    print(f'#{tc} {result}')