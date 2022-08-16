def spinArr(array): # 배열을 90도 돌리는 함수
    a = len(array)
    new_arr = [[0] * a for _ in range(a)]

    for i in range(a):
        for j in range(a):
            new_arr[j][a-i-1] = array[i][j]
    return new_arr # 돌린 배열을 return

for tc in range(1, int(input())+1):
    n, m = map(int,input().split()) # n : 배열 크기, m: 찾고자하는 회문의 길이
    arr = [list(input()) for _ in range(n)] # 배열 받아오기
    spin_arr = spinArr(arr) # 회전된 배열 선언 (열 방향으로 회문 찾기 위해)
    result = '' # 결과값 담을 변수

    for i in range(n): # 배열 전체 확인
        for j in range(n-m+1):
            check_col = arr[i][j:j+m]
            check_row = spin_arr[i][j:j+m]
            if check_col == check_col[::-1]: # 행 방향으로 회문인지 확인
                result = check_col
            if check_row == check_row[::-1]: # 열 방향으로 회문인지 확인
                result = check_row

    print(f"#{tc} {''.join(result)}")