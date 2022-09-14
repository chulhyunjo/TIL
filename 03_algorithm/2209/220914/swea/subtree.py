def pre(i):
    global cnt
    if i:
        cnt+=1
        pre(ch1[i])
        pre(ch2[i])

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    V = E + 1
    arr = list(map(int,input().split()))
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 0
    pre(N)
    print(f'#{tc} {cnt}')