T = int(input())
for tc in range(1, T+1):
    n,p = map(int, input().split())
    a = n // p
    b = n % p
    result = 1
    for _ in range(b):
        result *= (a+1)
    for _ in range(p-b):
        result *= a
    print(f'#{tc} {result}')