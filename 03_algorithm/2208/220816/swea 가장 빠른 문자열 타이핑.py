for tc in range(1,int(input())+1):
    a, b = input().split()

    i = 0 # 검사할 인덱스 위치
    cnt = 0 # 타이핑 횟수
    while i < len(a):
        check = a[i:i+len(b)] # 확인할 단어 슬라이싱
        if check == b: # 확인할 단어가 b와 같을 경우 실행
            cnt += 1 # 타이핑 횟수 +1
            i += len(b) # 인덱스를 확인한 단어 끝으로 이동
        else: # 아닐경우
            cnt += 1 # 타이핑 횟수 +1
            i += 1 # 인덱스를 1칸 뒤로 이동

    print(f'#{tc} {cnt}')