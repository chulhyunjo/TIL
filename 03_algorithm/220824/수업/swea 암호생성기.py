for _ in range(10):
    tc = int(input())
    arr = list(map(int,input().split()))

    cnt = 1
    while arr[-1] > 0:                                  # 마지막 요소가 0보다 같거나 작을때 까지 실행
        x = arr.pop(0)
        if x - cnt <= 0:                                # 0 보다 작으면 0으로 유지
            arr.append(0)
        else:
            arr.append(x-cnt)                           # 0 보다 크면 뒤로 넣기
        cnt = (cnt + 1) % 5 if (cnt+1) % 5 != 0 else 5  # 1사이클은 1~5 를 빼준다

    print(f'#{tc}', end = ' ')
    print(*arr)