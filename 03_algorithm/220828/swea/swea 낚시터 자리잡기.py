for tc in range(1,int(input())+1):
    n = int(input())
    gates = [list(map(int,input().split())) for _ in range(3)]
    result = 3600

    for _ in range(3):
        gate = gates.pop(0)
        gates.append(gate)
        space = [0] * n
        for _ in range(3):
            gate = gates.pop(0)
            gates.append(gate)
            num, p = gate[0] - 1, gate[1]
            cnt = 0
            dis = 0
            while cnt!=p:
                if 0 <= num - dis < n and not space[num-dis]:
                    space[num-dis] = dis + 1
                    cnt += 1
                    if cnt == p:
                        continue
                if 0 <= num + dis < n and not space[num+dis]:
                    space[num+dis] = dis + 1
                    cnt += 1
                dis += 1

        result = min(result, sum(space))

    print(result)