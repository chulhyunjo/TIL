for tc in range(1,int(input())+1) : # 테스트케이스 개수 입력
    laser = input() # 검사할 레이저 입력
    cnt = 0 		# 현재 쇠막대기의 개수를 담을 변수
    result = 0		# 총 몇개의 조각으로 잘리는지 담을 변수

    for i in range(len(laser) - 1):
        if laser[i] == '(':  # 현재 검사하는 괄호가 '('인지 검사
            if laser[i + 1] == '(':  # 다음 괄호가 '('인 경우 레이저 자리
                cnt += 1
            else:  # 아닌 경우 쇠막대기의 시작지점
                result += cnt

        else:
            if laser[i + 1] == ')' and cnt > 0:
                cnt -= 1
                result += 1