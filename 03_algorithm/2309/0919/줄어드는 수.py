# 문제 1
# 백트래킹
def chk(d, s):  # digit, string - 자릿수, 현재 숫자
    global cnt, flg
    if d < 0:
        if cnt == N:
            flg = 0
            print(s)
        cnt += 1
        return
    k = int(s[-1]) if s else 10
    for i in range(k):
        if i < d:   # 백의 자리수에서 2가 들어가는 것처럼 불가능한 경우 쳐내기
            continue
        chk(d-1, s+str(i))    # 마지막 숫자보다 작은 수 붙여가며 경우의 수 찾기

N = int(input())
cnt, flg = 1, 1
for i in range(10):   # 한 자릿수 부터 출발
    chk(i, '')
if flg:
    print(-1)