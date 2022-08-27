for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = []
    for _ in range(3):
        arr = list(map(list, zip(*arr[::-1])))
        result.append(arr)
    print(f'#{tc}')
    for i in range(n):
        for j in range(3):
            for k in result[j][i]:
                print(k, end= '')
            print(' ', end='')
        print()