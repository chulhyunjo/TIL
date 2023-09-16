def solution(A, S):
    # 배열의 길이
    N = len(A)
    answer = 0

    # 각 구간합
    arr_sum = [0] * (N + 1)

    for i in range(1, N + 1):
        arr_sum[i] = arr_sum[i - 1] + A[i - 1]

    print(arr_sum)
    for i in range(N):
        for j in range(i + 1, N + 1):
            # 현재 구간합
            sum1 = arr_sum[j] - arr_sum[i]
            cnt = j - i  # 구간 숫자 개수
            if sum1 == cnt * S:
                answer += 1

    return answer

# print(solution([i for i in range(1, 100001)], 20))
print(solution([1,5,3,4,2,6,7,7,93,28,7,47372,823,4928,72,83189,8132,8421,724,2417,235], 20))