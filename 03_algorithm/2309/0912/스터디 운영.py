N, K = map(int,input().split())

plan = [list(map(int,input().split())) for _ in range(N)]

# 각 K날짜에 몇명이 참여 안하는지 저장
people = [0] * K
for i in range(K):
	for j in range(N):
		if plan[j][i] == 0:
			people[i] += 1

# 전체 인원의 절반
half = N // 2 if N % 2 == 0 else N // 2 + 1
# 절반 이상인 날은 미뤄진다
answer = 0
for i in range(K):
	if people[i] >= half:
		answer += 1

print(answer)