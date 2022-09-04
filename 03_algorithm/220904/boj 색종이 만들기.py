def check(x, y, n):
    global blue, white
    now_color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != now_color:
                check(x, y, n//2)
                check(x + n//2, y, n//2)
                check(x, y + n//2, n//2)
                check(x + n//2, y + n//2, n//2)
                return
    if now_color == 1:
        blue += 1
    if now_color == 0:
        white += 1



n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
blue = white = 0
check(0,0,n)
print(white, blue,sep='\n')