for tc in range(1, int(input()) + 1):
    number = list(map(int, input()))
    max_number = list(number)
    min_number = list(number)
    max_idx = 0
    min_idx = 0
    # 최소
    for i in range(len(number)-1):
        min_num = number[i]
        for j in range(i+1, len(number)):
            if min_num >= number[j]:
                if i == 0 and number[j] == 0:
                    continue
                else:
                    min_idx = j
                    min_num = number[j]
        if min_num != number[i]:
            min_number[i], min_number[min_idx] = min_number[min_idx], min_number[i]
            break

    # 최대
    for i in range(len(number)-1):
        max_num = number[i]
        for j in range(i+1, len(number)):
            if max_num <= number[j]:
                max_idx = j
                max_num = number[j]
        if max_num != number[i]:
            max_number[i], max_number[max_idx] = max_number[max_idx], max_number[i]
            break
    max_number = list(map(str, max_number))
    min_number = list(map(str, min_number))
    print(f'#{tc}', ''.join(min_number), ''.join(max_number))
