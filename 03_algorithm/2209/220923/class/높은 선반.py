def find_top(d,t):
    global minV
    if t-B>=0:
        if t < minV:
            minV = t
    elif d < N and people[d]+t <= minV:
        find_top(d+1, t+people[d])
    if d<N-1:
        find_top(d+1,t)


for tc in range(1,int(input())+1):
    N, B = map(int,input().split())
    people = sorted(list(map(int,input().split())))
    used = [0] * N
    minV = 200000
    find_top(0,0)
    print(f'#{tc} {minV-B}')