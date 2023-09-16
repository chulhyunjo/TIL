def solution(blocks):
    # return max(K- J + 1)
    # 다음 블록이 현재 높이와 같거나, 더 큰경우만 이동가능
    # 2 <= N <= 200000
    # 각 원소 크기 1 ~ x ~ 1000000000

    N = len(blocks)

    # -> 방향 오름차순(같아도 포함) 개수
    cnt1 = [1] * N
    # <- 방향 오름차순(같아도 포함) 개수
    cnt2 = [1] * N

    # -> 방향 채우기
    for i in range(N - 2, -1, -1):
        if blocks[i] <= blocks[i + 1]:
            cnt1[i] = cnt1[i + 1] + 1

    # <- 방향 채우기
    for i in range(1, N):
        if blocks[i] <= blocks[i - 1]:
            cnt2[i] = cnt2[i - 1] + 1

    answer = 0
    for i in range(N):
        answer = max(answer, cnt1[i] + cnt2[i] - 1)

    return answer
