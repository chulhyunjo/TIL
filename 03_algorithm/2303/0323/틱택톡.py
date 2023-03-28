from collections import deque
dx = [3, 0, 3 ,-3]
dy = [0, 1, 1, 1]

while True:
    board = input()
    if board == 'end':
        break
    board = list(board)
    cnt_X = board.count("X")
    cnt_O = board.count("O")
    cnt_no = board.count('.')
    if cnt_X - cnt_O >1:
        print("invalid")
        continue
    if cnt_O > cnt_X:
        print('invalid')
        continue

    finished_X = 0
    finished_O = 0
    for move in range(4):
        for i in range(9):
            if board[i] == ".": continue
            if dy[move] and (i+dy[move])%3==0: continue
            else: next = i+ dy[move]
            next += dx[move]
            if next>=9 or next<0: continue
            if board[next] == board[i]:
                if dy[move] and (next + dy[move]) % 3 == 0:
                    continue
                else:
                    next += dy[move]
                next +=dx[move]
                if next >= 9 or next < 0: continue
                if board[next] == board[i]:
                    if board[i] == 'X':
                        finished_X+=1
                    if board[i] == 'O':
                        finished_O+=1

    if finished_O and finished_X:
        print('invalid')
        continue
    elif finished_O and cnt_X > cnt_O:
        print('invalid')
        continue
    elif finished_X and cnt_X == cnt_O:
        print('invalid')
        continue
    elif finished_O == 0 and finished_X == 0 and cnt_no:
        print('invalid')
        continue
    else:
        print('valid')
        continue