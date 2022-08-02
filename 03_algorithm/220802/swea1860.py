def count_bread(N, customer, M, K):
    for i in range(N):
        total_bread = (customer[i] // M) * K
        if total_bread < i + 1:
            return 'Impossible'
    return 'Possible'


for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    array = sorted(list(map(int, input().split())))
    result = count_bread(n, array, m, k)
    print(f'#{tc} {result}')
