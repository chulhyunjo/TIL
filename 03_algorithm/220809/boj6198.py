import sys
n = int(sys.stdin.readline())

buildings = []

for _ in range(n):
    buildings.append(int(sys.stdin.readline()))

count = 0
# 비교할 대상의 빌딩 리스트
next_buildings = []
for i in range(1, n):
    # 비교 대상 빌딩 리스트에 현재 빌딩 리스트의 마지막 빌딩 빼서 넣기
    next_buildings.append((buildings.pop(), i))
    while next_buildings and (next_buildings[-1][0] < buildings[-1]):
        # 비교 대상 빌딩이 더 작으면 비교 대상 빌딩 리스트에서 빼기
        next_buildings.pop()

    print(next_buildings)

    if next_buildings:
        count += i - next_buildings[-1][1]
        # 비교할 빌딩이 남아있지 않다면 현재의 인덱스 더하기
    else:
        count += i

print(count)
