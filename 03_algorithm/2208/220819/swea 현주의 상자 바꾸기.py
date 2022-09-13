for tc in range(1, int(input())+1):
    n, q = map(int,input().split())
    box = [0] * n
    for i in range(1,q+1):
        r, l = map(lambda x: x-1,map(int,input().split()))
        for j in range(r,l+1):
            box[j] = i

    print(f'#{tc}', end = ' ')
    print(*box)