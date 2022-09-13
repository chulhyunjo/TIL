for tc in range(1, int(input()) + 1):
    number, n = map(int, input().split())
    number_list = []
    for i in str(number):
        number_list.append(int(i))
    max_idx = 0
    max_number = list(number_list)
    # 최대
    cnt = 0
    for i in range(len(number_list)):
        max_num = max_number[i]
        for j in range(i + 1, len(number_list)):
            if max_num <= max_number[j]:
                max_idx = j
                max_num = number_list[j]
        if max_num != max_number[i]:
            max_number[i], max_number[max_idx] = max_number[max_idx], max_number[i]
            cnt+=1
        if cnt == n:
            break
    if cnt != n:
        for i in range(n-cnt):
            max_number[-1] , max_number[-2] = max_number[-2], max_number[-1]

    max_number = list(map(str, max_number))
    print(f'#{tc}',''.join(max_number))