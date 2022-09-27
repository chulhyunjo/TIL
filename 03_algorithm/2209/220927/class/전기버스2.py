def search(i,n):
    global minV
    if i > len(bus)-1:
        minV = min(n, minV)
    elif n > minV:
        return
    else:
        for m in range(bus[i], 0, -1):
            search(i+m, n+1)

for tc in range(1, int(input())+1):
    n, *bus = map(int,input().split())
    minV = 100
    search(0,-1)
    print(f'#{tc} {minV}')