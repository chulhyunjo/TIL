import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 이진 검색 트리는 왼쪽으로 갈 수록 작은수, 오른쪽을 큰 수 이다.
def post(start, end):
    if start > end:
        return
    mid = end + 1               # 오른쪽 자식이 없는 경우를 대비하기 위해 mid = end+1로 먼저 설정해 준다.
    for i in range(start, mid): # 시작부터 끝까지 탐색
        if A[start] < A[i]:     # 왼쪽에는 작은 값들이 나오므로 큰값이 나올 경우 오른쪽 자식으로 판정
            mid = i             # 오른쪽 자식이 되는 노드의 위치를 mid에 저장
            break

    post(start+1, mid-1)        # 왼쪽 자식들을 다시 탐색
    post(mid, end)              # 왼쪽끝나고 오른쪽 탐색
    print(A[start])             # 후위 순회: 왼쪽->오른쪽->중간

A = []
while True:                     # 입력 받기
    try:
        A += [int(input().rstrip())]
    except:
        break
post(0, len(A)-1)