for tc in range(1, int(input())+1):
    n = int(input())                                # 배열 크기 받기
    arr = [[1] * i for i in range(1,n+1)]           #   리스트 생성

    for i in range(2, n):                           # 2중 for문으로 파스칼 삼각형 만들기
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j] # 위에 왼쪽 위에 오른쪽 원소의 합이 현재 원소

    print(f'#{tc}')
    for i in arr:
        print(*i)

