def solution(A, S):

    def fragment(idx, lastIdx, numSum, numCnt):
        nonlocal answer

        # continuous fragment 완성한 경우
        if idx == N or (lastIdx >= 0 and lastIdx < idx - 1):
            if numCnt > 0 and numSum/numCnt == S:
                answer += 1
            return

        if lastIdx < 0 or lastIdx == idx - 1:
            fragment(idx+1, idx, numSum+A[idx], numCnt+1)
        fragment(idx+1, lastIdx, numSum, numCnt)

    N = len(A)
    answer = 0
    fragment(0, -1, 0, 0)

    return answer
