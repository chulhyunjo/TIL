def game(x, y): # x,y 인덱스 가위바위보 실행
    if (arr[x] - arr[y]) in [-2, 1] or arr[x] == arr[y]:    # (가위 - 바위 = -2), (바위-가위,보-바위) = 1, 같으면 왼쪽
        return x
    else:
        return y


def play(l, r): # 왼쪽, 오른쪽 토너먼트 함수
    if l == r:  # 왼쪽, 오른쪽이 같으면 최종 승자
        return l
    else:
        mid = (l + r) // 2          # 중간 인덱스

        left = play(l, mid)         # 중간을 기준으로 왼쪽 최종 승자 담기
        right = play(mid+1, r)      # 중간을 기준으로 오른쪽 최종 승자 담기
        return game(left,right)     # 왼쪽,오른쪽 가위바위보 실행해서 승자 얻기 재귀
                                    # 마지막에 중간을 기준으로 왼쪽 최종 승자 vs 오른쪽 최종승자 -> 우승자


for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int,input().split()))

    print(f'#{tc} {play(0,n-1)+1}') # 최종 우승자의 인덱스를 뽑아와야 하므로 idx+1