n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum1 = 0
for i in score:
    new_score = i / max_score * 100
    sum1 += new_score

result = sum1 / len(score)
print(result)