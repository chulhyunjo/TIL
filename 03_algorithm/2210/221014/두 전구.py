for tc in range(1, int(input())+1):
    a,b,c,d = map(int,input().split())
    arr = [0] * 101
    for i in range(a,b):
        arr += 1
    for j in range(c,d):
        arr += 1
    print(f'#{tc} {arr.count(2)}')