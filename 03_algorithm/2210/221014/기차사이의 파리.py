for tc in range(1, int(input())+1):
    d, a, b, f = map(int,input().split())
    time = d / (a+b)
    result = time*f
    print(f'#{tc} {result}')