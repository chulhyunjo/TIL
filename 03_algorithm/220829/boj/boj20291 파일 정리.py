import sys
input = sys.stdin.readline              # 총 파일 케이스가 50000개까지 나와서 stdin.readline 이용
n = int(input())                        # 파일의 총 개수
result = dict()                         # 확장자 이름을 담을 딕셔너리 생성
for _ in range(n):
    a, b = input().rstrip().split('.')  # a: 파일 이름, b: 확장자 이름 -> spilt('.')를 이용해서 처음부터 분배
    if b not in result:                 # 현재 확장자가 딕셔너리에 없는 경우
        result[b] = 1                   # 현재 확장자 생성 후 1개로 표시
    else:                               # 이미 있는 경우
        result[b] += 1                  # 개수 1개 증가

for k,v in sorted(result.items()):      # k(키): 확장자 이름, v(값): 개수
    print(k,v)