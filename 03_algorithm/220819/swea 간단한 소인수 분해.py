for tc in range(1, int(input())+1):
    num = int(input())                  # 소인수 분해할 자연수 입력
    numbers = [2,3,5,7,11]              # 나눌 값을 담은 리스트
    cnt = [0] * 5                       # 개수를 담을 리스트
    for i in range(5):                  # 5개의 숫자로 소인수 분해
        while num % numbers[i] == 0:    # 나눠진다면 아래 실행
            cnt[i] += 1                 # cnt리스트에 추가
            num //= numbers[i]          # num을 나눈값으로 초기화

    print(f'#{tc}', end = ' ')
    print(*cnt)