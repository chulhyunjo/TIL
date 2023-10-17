from collections import deque


def solution(n):
    # 알 queue [알 깨지는 시간, 개수]
    egg = deque([(2, 1)])
    # 현재 알의 개수
    egg_cnt = 1
    time = 0

    # 드래곤 queue
    dragon = deque()
    # 현재 드래곤 수
    dragon_cnt = 0
    # 알을 낳지 못하는 드래곤 수
    can_not_dragon = 0

    # n시간동안 진행
    while time <= n:
        # 현재 알이 있고 알이 부화할 시간이면 부화
        while egg and time == egg[0][0]:
            e_t, e_c = egg.popleft()
            # dragon = [알을 낳을 수 있는 시간, 드래곤 개수]
            dragon.append((e_t + 3, e_c))
            # 현재 알 개수 뺀다
            egg_cnt -= e_c
            # 현재 드래곤 수 더한다
            dragon_cnt += e_c

        # 알을 낳을 수 있는 드래곤이 있다면 알을 낳는다
        if dragon_cnt - can_not_dragon > 0:
            egg.append((time + 2, dragon_cnt - can_not_dragon))
            egg_cnt += dragon_cnt - can_not_dragon

        # 알을 낳지 못하는 알은 queue에서 빼기
        while dragon and time == dragon[0][0]:
            t, c = dragon.popleft()
            can_not_dragon += c

        time += 1

    return egg_cnt + dragon_cnt