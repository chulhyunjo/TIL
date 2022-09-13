for tc in range(1, int(input())+1):
    a, b, c, d = map(int,input().split())
    result = min(b,d) - max(a,c)
    if result > 0:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} 0')
