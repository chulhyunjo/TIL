for tc in range(1, int(input())+1):
    arr = [[0]*10 for _ in range(10)]
    n = int(input())
    cnt = 0 # 작업 횟수 담을 변수
    for _ in range(n):
        x1, y1, x2, y2 = map(int,input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if arr[i][j] == 0: # 작업하지 않은 타일 일때
                    arr[i][j] = 1 # 타일을 1로 바꿔 작업한 타일이라 표시
                    cnt += 1 # 작업 횟수 증가

    print(f'#{tc} {cnt}')