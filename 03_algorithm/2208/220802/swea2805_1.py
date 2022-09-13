for tc in range(1, int(input())+1):
    n = int(input())
    # 리스트를 담을 array 선언
    array = [list(map(int,input())) for _ in range(n)]
    half = n // 2
    result = 0

    # 중간을 기준으로 위로
    for i in range(n//2):
        result += sum(array[i][half - i : half + i + 1])

    # 배열을 뒤집기
    array.reverse()
    for i in range(n//2):
        result += sum(array[i][half - i : half + i + 1])

    # 중간
    result += sum(array[half])

    print(f'#{tc} {result}')