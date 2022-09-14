def make(i):
    global number
    if i <= N:
        make(i*2)
        tree[i] = number
        number += 1
        make(i*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    number = 1
    make(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
