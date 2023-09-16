def solution(A):
    # i만큼 i번 들어있는 최대 값
    # A의 크기 1~10,0000

    # 이부분에서 틀림,, 범위 설정 잘못함
    cnt = [0] * 100001

    N = len(A)
    for i in range(N):
        # if A[i] > 100000: continue 추가해줘야함
        cnt[A[i]] += 1

    max_number = 0
    for i in range(1, 100001):
        if cnt[i] == i:
            max_number = i

    return max_number