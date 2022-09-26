T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus = [0] * 5001
    for _ in range(N):
        a, b = map(int,input().split())
        for i in range(a, b+1):
            bus[i] += 1

    P = int(input())
    print(f'#{tc}', end = ' ')
    for _ in range(P):
        c = int(input())
        print(f'{bus[c]}', end = ' ')
    print()