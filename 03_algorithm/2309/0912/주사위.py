N, T = map(int,input().split())
numbers = list(map(int,input().split()))

max_number = max(numbers) # 주사위의 가장 큰 값
min_number = min(numbers) # 주사위의 가장 작은 값

# 최소 횟수 = T에서 가장 큰값을 나눈 횟수(나눠지면) else T에서 가장 큰값을 나눈 횟수 + 1
min_answer = T // max_number if T % max_number == 0 else T // max_number + 1
# 최대 횟수 = T에서 가장 작은값을 나눈 횟수(나눠지면) else T에서 가장 작은값을 나눈 횟수 + 1
max_answer = T // min_number if T % min_number == 0 else T // min_number + 1

print(min_answer, max_answer)