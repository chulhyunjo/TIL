dx = [1, -1]
dy = [1, -1]

w,h = map(int,input().split())
p, q = map(int,input().split()) # 초기 위치
tm = int(input())
mp = tm - (w-p)
mq = tm - (h-q)

print(abs(w - mp%(2*w)),abs(h - mq%(2*h)))