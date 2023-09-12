N, M = map(int,input().split())
word = input()

# [A~Z]를 리스트로 만든다
keyword = [chr(i) for i in range(ord('A'), ord('Z')+1)]

# 고장난 알파벳 <-> 출력되는 알바벳 교체
for _ in range(M):
	A, B = input().split()
	keyword[ord(A) - 65] = B
	keyword[ord(B) - 65] = A

# 하나씩 눌러보기
answer = [''] * N
for i in range(N):
	w = word[i]
	answer[i] = keyword[ord(w)-65]

print(''.join(answer))
