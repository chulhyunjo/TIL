for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    min_sum = 1000001 # 구간 최소 합 담을 변수 최대값(10000 * 100)보다 큰 1000001
    max_sum = 0 # 구간 최대 합 담을 변수

    for i in range(n-m+1): # n-m 번 만큼 반복
        sum_arr = arr[i:i+m] # 구간 합을 계산할 범위
        sum1 = 0 # 현재 구간 합 담을 변수
        for j in sum_arr:
            sum1 += j # 구간합 구하기

        if min_sum > sum1:
            min_sum = sum1
        if max_sum < sum1:
            max_sum = sum1

    result = max_sum - min_sum
    print(f'#{tc} {result}')