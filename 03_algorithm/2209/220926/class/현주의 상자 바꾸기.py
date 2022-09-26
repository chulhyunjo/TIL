T = int(input())
for tc in range(1,T+1):
    n, q = map(int,input().split())
    box = [0] * (n+1)
    for i in range(1,q+1):
        L, R = map(int,input().split())
        box[L:R+1] = [i] * (R-L+1)
    print(f'#{tc}', *box[1:])