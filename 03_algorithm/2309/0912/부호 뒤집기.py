N = map(int,input().split())
numbers = list(map(int,input().split()))

# 현재 수열의 전체 합
sum1 = sum(numbers)

# 가장 낮은 숫자를 바꿔줘야 한다.
min_number = min(numbers)

# 정답 = 전체합 - 가장 작은숫자 + (-가장 작은 숫자)
answer = sum1 - min_number - min_number

print(answer)
