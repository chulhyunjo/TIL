N, D = map(int,input().split())

# 각 시간을 담을 리스트
time = []
# 각 시간을 분으로 변환에서 저장
for _ in range(N):
	H, M = map(int,input().split())
	m = H * 60 + M
	time.append(m)

# 두개씩 짝지어서 D차이 나는지 확인
flag = 0
answer = [0,0]
for i in range(N):
	for j in range(i+1, N):
		if abs(time[i] - time[j]) == D:
			answer[0] = i + 1
			answer[1] = j + 1
			flag = 1
			break
	if flag:
		break

print(answer[0], answer[1])