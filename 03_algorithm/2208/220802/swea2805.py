for tc in range(1, int(input())+1):
    n = int(input())
    array = [list(map(int,input())) for _ in range(n)]
    half = n //2
    result = 0

    # 중간을 기준으로 위로
    for i in range(n//2):
        result += sum(array[i][half - i : half + i + 1])

    # 중간을 기준으로 아래
    for i in range(1, n//2 + 1):
        result += sum(array[-i][half - i + 1 : half + i])

    # 중간
    result += sum(array[half])

    print(f'#{tc} {result}')