for tc in range(1, int(input())+1):
    n, m = map(int,input().split())             # n : 화덕 크기, m: 피자 크기
    pizza = list(map(int,input().split()))      # 피자들 리스트 받기
    queue = []
    for i in range(m):
        queue.append((i+1,pizza[i]))            # (피자 번호, 치즈양) 담기

    cook = []                                   # 화덕
    for j in range(n):
        cook.append(queue.pop(0))               # 화덕의 크기만큼 1~n까지 넣기

    while len(cook) != 1:                       # 화덕안에 피자의 개수가 1일때 까지 실행
        num, cheese = cook.pop(0)               # 현재 번호, 치즈 양 뽑기 -> 화덕 입구
        if cheese // 2:                         # 치즈가 다 녹지 않았으면
            cook.append((num,cheese//2))        # 반이 녹은 값을 다시 화덕에 넣기
                                                # 다 녹았으면
        if queue and len(cook) != n:            # 현재 구워야할 피자가 남아있고 화덕의 자리가 남아있다면
            cook.insert(0,queue.pop(0))         # 화덕에 다음피자 넣기

    print(f'#{tc} {cook[0][0]}')                # 남은 피자의 번호 출력