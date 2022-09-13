import math

def check_distance(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return result

def check_line(point1, point2, op):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    a, b = op[0], op[1]
    area = abs((x1- a) * (y2 - b) - (x2- a) * (y1 - b))
    line = check_distance(point1, point2)
    result = area / line if area else False
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    if x1 < a < x2 and y1 < b < y2:
        return result <= 5.73
    else:
        return False

def check_hit_angle(white, point, goal):
    a = check_distance(white, point)
    b = check_distance(point, goal)
    c = check_distance(white, goal)
    return c**2 > a**2 + b**2


def find_point(point, goal):
    x1, y1 = point[0], point[1]
    x2, y2 = goal[0], goal[1]
    distance = check_distance(point, goal)
    point_distance = distance + 5.73
    point_x = abs(x2 -abs(x1-x2) * point_distance / distance)
    point_y = abs(y2 -abs(y1-y2) * point_distance / distance)
    return [point_x, point_y]


def find_cusion(white, target, goal):
    cusion_x = (white[0] + target[0]) / 2
    cusion_y = (white[1] + target[1]) / 2
    a, b = goal[0], goal[1]
    # 아래 쿠션만 탐색
    return [[cusion_x, 0], [cusion_x, 130], [0, cusion_y], [260, cusion_y]]

def check_angle(white, target):
    x1, y1 = white[0], white[1]
    x2, y2 = target[0], target[1]
    result = math.degrees(math.atan2(x2-x1, y2-y1))
    return result

player = 1
goals = [[0,0], [0, 130], [260,0], [0,130], [130, 130], [260, 130]]
balls = [[20,20], [30, 30], [0, 0] , [0, 0], [0, 0], [100, 100]]
white_ball = balls[0]
if player == 1:
    target_balls = [balls[1], balls[3]]
    op_balls = [balls[2], balls[4], balls[5]]
    black_ball = balls[5]
else:
    target_balls = [balls[2], balls[4]]
    op_balls = [balls[1], balls[3], balls[5]]
    black_ball = balls[5]

result_goal = []
result_target = []
result_target_point = []
for goal in goals:
    for target in target_balls:
        if target[0] != 0 or target[1] != 0:
            break
    else:
        target_point = find_point(black_ball, goal)
        if check_hit_angle(white_ball, target_point, goal):
            for op_ball in op_balls:
                if op_ball[0] == 0 and op_ball[1] == 0:
                    continue
                if check_line(white_ball, target_point, op_ball):
                    break
                if check_line(black_ball, goal, op_ball):
                    break
                result_goal = goal
                result_target = black_ball
                result_target_point = target_point
        if result_goal:
            break
    for target in target_balls:
        if not target[0] and not target[1]: continue
        target_point = find_point(target, goal)
        if check_hit_angle(white_ball, target_point, goal):
            for op_ball in op_balls:
                if op_ball[0] == 0 and op_ball[1] == 0:
                    continue
                if check_line(white_ball, target_point, op_ball):
                    break
                if check_line(target, goal, op_ball):
                    break
                result_goal = goal
                result_target = target
                result_target_point = target_point
        if result_goal:
            break
    if result_goal:
        break

if not result_goal:
    for goal in goals:
        for target in target_balls:
            if not target[0] and not target[1]: continue
            target_point = find_point(target, goal)
            cusions = find_cusion(white_ball, target_point, goal)
            for cusion in cusions:
                if cusion in goals: continue
                if check_hit_angle(cusion, target_point, goal):
                    for op_ball in op_balls:
                        if op_ball[0] == 0 and op_ball[1] == 0:
                            continue
                        if check_line(white_ball, cusion, op_ball):
                            break
                        if check_line(cusion, target_point, op_ball):
                            break
                        if check_line(target, goal, op_ball):
                            break
                        result_goal = goal
                        result_target = target
                        result_target_point = target_point
                if result_goal:
                    break
            if result_goal:
                break
        if result_goal:
            break

print(white_ball, result_target_point)
print(result_target, result_goal)
angle = check_angle(white_ball, result_target_point)
if angle < 0:
    angle = 360 + angle

print(angle)