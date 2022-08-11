for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    time = 0 # 흐른 시간 담을 변수
    while time < m: # m초 까지 반복
        time += 1 # 1번 반복하면 1초 증가
        for i in range(n):
            for j in range(n):
                if m % time == 0: # m이 time의 배수일 때 (2)실행하지 않고 전체 토글
                    arr[i][j] = 1 if arr[i][j] == 0 else 0 # 토글

                elif (i+j+2) % time == 0:   # i,j 인덱스의 배수 일 경우
                                            # i,j는 문제에서 1로 시작해서 +2을 해준다
                    arr[i][j] = 1 if arr[i][j] == 0 else 0 # 토글

    cnt = 0  # 1의 개수를 담을 변수
    for i in range(n): # 전체 리스트 돌며 1를 센다
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
    print(f'#{tc} {cnt}')