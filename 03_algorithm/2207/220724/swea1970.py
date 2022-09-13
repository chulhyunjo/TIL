for tc in range(int(input())):
    change = int(input())
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{tc+1}')
    for money in moneys:
        cnt = 0
        cnt += change // money
        change %= money
        print(cnt, end = ' ')
    print()
