for tc in range(1, int(input())+1):
    n = int(input())
    cnt = [0] * 5001
    for _ in range(n):
        a, b = map(int,input().split())
        for i in range(a,b+1):
            cnt[i] += 1

    p = int(input())
    print(f'#{tc}', end = ' ')
    for _ in range(p):
        j = int(input())
        print(cnt[j], end = ' ')
    print()