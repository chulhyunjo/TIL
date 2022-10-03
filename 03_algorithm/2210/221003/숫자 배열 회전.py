T = int(input())
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    spin = []
    for _ in range(3):
        graph = list(map(list,zip(*graph[::-1])))
        spin.append(graph)
    print(f'#{tc}')
    new = list(map(list,zip(*spin)))
    for i in range(n):
        now = new[i]
        for j in range(3):
            for k in range(n):
                print(now[j][k], end = "")
            print("", end=" ")
        print()