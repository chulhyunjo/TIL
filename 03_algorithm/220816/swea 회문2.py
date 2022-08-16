def spin_array(array): # 배열을 회전 시키는 함수 (세로 방향 확인을 위해)
    new_array = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            new_array[j][100-i-1] = array[i][j]
    return new_array


for _ in range(10):
    tc = int(input())                               # 테스트 넘버
    arr = [list(input()) for _ in range(100)]       # 2차원 배열
    spin_arr = spin_array(arr)                      # 회전시킨 배열 생성 (세로방향 확인)
    result = 0
    for k in range(100, 0, -1):                   # k 길이 만큼 확인# 최대수 담을 변수
        for i in range(100):                            # 모든 행 확인
            for j in range(100-k):                        # 각 행에서 시작지점
                word_col = arr[i][j:j+k]            # 가로 방향 단어
                word_row = spin_arr[i][j:j+k]       # 세로 방향 단어
                if k <= result:                      # k가 최대 수 보다 작으면 break
                    break
                if word_col == word_col[::-1]:      # (가로방향) 회문이면 실행
                    result = k if result < k else result # k값이 현재 최대값보다 크면 초기화
                    break
                if word_row == word_row[::-1]:      # (세로방향) 회문이면 실행
                    result = k if result < k else result # k값이 현재 최대값보다 크면 초기화
                    break

    print(f'#{tc} {result}')
