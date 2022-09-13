s0 = 3                      # S(0)일때 moo의 길이 = 3
cnt = 1
n = int(input())            # 찾고자 하는 n번째 자리수 입력
s = [s0]                    # S(x) x에 따른 moo의 길이를 담을 리스트
while s0 < n:
    s0 += s0 + (cnt + 3)    # moo게임의 문자열 길이는 S(x) + (k+3) + S(x)
    cnt += 1
    s.append(s0)            # 리스트에 담기
for q in range(cnt-1,0,-1):
    mid = s[q] - s[q-1] * 2 # S(x) + (k+3) + S(x)에서 중간 (k+3)의 문자열 길이를 담을 변수
    if s[q-1] > n:          # 첫 S(x)위치에 존재할 경우 continue
        continue
    if n - s[q-1]<=mid:     # 찾고자하는 문자열의 위치가 S(x)+ (k+3)에서 (k+3)위치에 존재 할 경우
        n -= s[q-1]         # (k+3)중에서 몇번째 자리인지 확인
        break
    else:
        n -= (s[q-1] + mid) # S(x)+(k+3)보다 클 경우 S(x) + (k+3) 만큼 뺀다
                            # S(x)에서 몇번째 자릿수인지 확인하기 위함

if not n-1:                 # (k+3)중에 첫번째 자리일 경우 'm'
    print('m')
else:                       # 나머지는 'o'
    print('o')