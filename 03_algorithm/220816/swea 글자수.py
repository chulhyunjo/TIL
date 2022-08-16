for tc in range(1,int(input())+1):
    word1 = set(input())
    word2 = input()
    result = 0 # 결과 값

    for i in word1:
        cnt = 0  # 개수 세기
        for j in word2:
            if i == j:
                cnt += 1

        if cnt > result:
            result = cnt

    print(f"#{tc} {result}")