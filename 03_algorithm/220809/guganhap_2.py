for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    S = 0
    for i in range(m):  # 첫 부분합을 기준으로 다음 구간의 차이를 구해 새로운 리스트를 만든다.
        S += arr[i]

    minV = maxV = S  # 첫 부분합보다 가장 작은 값 차이 저장 (음수 값을 가짐)
    # 첫 부분합을 기준으로 다음 부분합와의 차이를 계속 더한다
    for j in range(n-m):
        S += (arr[j+m] - arr[j])
        if S < minV:
            minV = S
        if S > maxV:
            maxV = S
    result = maxV - minV

    print(f'#{tc} {result}')