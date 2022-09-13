for tc in range(1, int(input())+1):
    n = int(input())
    bus = [0] * 1001
    for _ in range(n):
        s, a, b = map(int,input().split())
        if s == 1:
            for i in range(a, b+1):
                bus[i] += 1
        elif s == 2:
            for i in range(a, b+1,2):
                bus[i] += 1
            if a % 2 and not b % 2:
                bus[b] += 1
            elif not a % 2 and b % 2:
                bus[b] += 1

        else:
            if not a % 2:
                for i in range(a,b+1):
                    if i%4:
                        continue
                    else:
                        bus[i] += 1
                if not b%4:
                    bus[b] += 1

            else:
                for i in range(a,b):
                    if not i % 3 and i % 10:
                        bus[i] += 1
                if b % 3 and not b % 10:
                    bus[b] += 1

    print(f'#{tc} {max(bus)}')