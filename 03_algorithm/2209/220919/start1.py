nums ={
    '0001101':0, '0011001':1,
    '0010011':2,'0111101':3,
    '0100011':4,'0110001':5,
    '0101111':6,'0111011':7,
    '0110111':8,'0001011':9
    }

for tc in range(1, int(input())+1):

    n, m = map(int,input().split())
    graph = [list(input()) for _ in range(n)]
    pattern = []

    for i in range(n):
        for j in range(m-1,-1,-1):
            if graph[i].count('1') == 0:
                continue
            if graph[i][j]=='1':
                pattern = graph[i][j-55:j+1]
                break
        if pattern: break

    code = ''
    odd = 0
    evn = 0
    for i in range(8):
        l = i*7
        if i % 2:
            evn += nums[''.join(pattern[l: l+7])]
        else:
            odd += nums[''.join(pattern[l: l+7])]

    result = odd*3 + evn
    print(f'#{tc}', end = ' ')
    print(0) if result % 10 else print(odd+evn)