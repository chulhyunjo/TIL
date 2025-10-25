# 특정 상황에서만 사용할 수 있다.
# 가장 작은 값, 가장 큰 값의 차이가 크지 않을때 100만 이하
# 정수형일 경우만

array = list(map(int,input().split()))

count = [0] * (max(array) + 1)

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = " ")
