def check(x, y, n):
    global blue, white
    now_color = paper[x][y] # 현재 위치의 색깔

    for i in range(x, x + n):               # 정사각형 크기 만큼 탐색
        for j in range(y, y + n):
            if paper[i][j] != now_color:    # 같은 색이 아니면 정사각형 x
                check(x, y, n//2)           # 4분의 1로 나눠 탐색 (1사분면)
                check(x + n//2, y, n//2)    # 3사분면
                check(x, y + n//2, n//2)    # 2사분면
                check(x + n//2, y + n//2, n//2) # 4사분면
                return
    if now_color == 1:                      # 정사각형이고 파란색이면
        blue += 1
    if now_color == 0:                      # 정사각형이고 흰색이면
        white += 1



n = int(input())     # NxN 색종이
paper = [list(map(int, input().split())) for _ in range(n)] # 색종이 입력
blue = white = 0    # 결과 값 받을 변수
check(0,0,n)        # n x n 크기의 색종이 확인
print(white, blue,sep='\n')