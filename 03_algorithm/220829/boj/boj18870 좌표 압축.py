n = int(input())                        # n개의 좌표
arr = list(map(int,input().split()))    # 좌표 리스트
checkArr = sorted(list(set(arr)))       # 정렬된 좌표 리스트(중복은 set로 제거)
result = dict()                         # 압축된 값을 딕셔너리에 담기위해 선언
for i in range(len(checkArr)):
    result[checkArr[i]] = i             # 차례대로 압축

for j in arr:
    print(f'{result[j]}', end = ' ')    # 출력