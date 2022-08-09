for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    arr = list(map(int, input().split()))
    new_arr = [0] * (n-m)

    for i in range(n-m): # 현재 부분합 - 다음 부분합의 차이를 구해 새로운 리스트에 담는다.
        new_arr[i] = arr[i] - arr[i+m]

    minV = 0 # (첫 부분합 - 가장 큰수) 저장
    maxV = 0 # (첫 부분합 - 가장 작은 수) 저장
    sum1 = 0 # sum1은 첫번째 부분합을 0을 기준으로 다음 부분합과의 차이를 담은 변수
    for j in new_arr:
        sum1 += j
        # m = 3 일경우
        # (arr[0] - arr[3]) + (arr[3] - arr[6]) + (arr[6] - arr[9]) ...
        # 하나씩 더하면 첫번째 부분합을 기준으로 차이를 알 수 있다.
        if sum1 < minV:
            minV = sum1
        if sum1 > maxV:
            maxV = sum1
    result = maxV - minV # (첫 부분합 - 가장 작은 수) - (첫 부분합 - 가장 큰 수) = 가장 큰 수 - 가장 작은 수
    print(f'#{tc} {result}')
