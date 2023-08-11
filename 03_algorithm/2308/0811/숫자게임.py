def solution(A, B):
    A.sort()
    B.sort()
    N = len(A)

    # 작은 수부터 확인
    a = 0
    b = 0
    answer = 0

    while a < N and b < N:
        # 현재 a팀원보다 b팀원이 높으면 answer + 1
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        # a 팀원이 더 클 때 b만 +1
        elif A[a] >= B[b]:
            b += 1

    return answer
