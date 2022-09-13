dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,word):
    if len(word) == 7:
        result.add(word)
        return

    word += arr[x][y]
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx,ny,word)


for tc in range(1, int(input())+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()
    s = ''
    for i in range(4):
        for j in range(4):
            dfs(i,j,s)

    print(f'#{tc} {len(result)}')