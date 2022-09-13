for tc in range(1, int(input())+1):                         # 테스트 케이스 개수 입력
    n, k = map(int,input().split())                         # nxn배열크기, k의 크기인 단어
    arr = [list(map(int,input().split())) for _ in range(n)]# 배열 입력
    result = 0                                              # 최종 결과
    for i in range(n):
        cnt = 0                                             # 현재 빈칸 개수 변수
        for j in range(n):
            if arr[i][j] == 1:                              # 빈칸이라면 cnt += 1
                cnt += 1
            if arr[i][j] == 0 or j == n-1:                  # 막힌칸, 끝지점이라면
                if cnt == k:                                # k크기의 단어일 경우 result += 1
                    result += 1
                cnt = 0                                     # cnt = 0 초기화

    for i in range(n):                                      # 위와 같은 방법 세로로 확인
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

    print(f'#{tc} {result}')