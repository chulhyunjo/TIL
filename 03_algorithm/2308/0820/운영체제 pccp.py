import heapq
def solution(program):
    N = len(program)
    program.sort(key=lambda x: x[1])

    pq = []

    cnt = 0
    time = 0
    answer = [0] * 11
    while True:
        while cnt < N and program[cnt][1] <= time:
            heapq.heappush(pq, (program[cnt][0], program[cnt][1], program[cnt][2]))
            cnt += 1
        if pq:
            a, b, c = heapq.heappop(pq)
            answer[a] += time - b
            time += c
            answer[0] = time
        else:
            time = program[cnt][1]

        if not pq and cnt == N:
            break

    return answer