import math


def point_distance(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result


def point_line_distance(point1, point2, op):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    a, b = op[0], op[1]
    area = abs((x1 - a) * (y2 - b) - (x2 - a) * (y1 - b))
    distance = point_distance(point1, point2)
    result = area / distance
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    if x1 < a < x2 and y1 < b < y2:
        return result <= 5.73
    else:
        return False


def is_in_range(point1, point2, goal):
    c = point_distance(point1, goal)
    a = point_distance(point2, goal)
    b = point_distance(point1, point2)
    if math.degrees(abs(math.atan2(goal[1] - point1[1], point1[0] - point2[0]))) + abs(math.degrees(math.atan2(goal[0] - point2[0], goal[1] - point2[1]))) >= 100:
        if c**2 > a**2 + b**2:
            return True
        else:
            return False
    else: return False
    # return c ** 2 > a ** 2 + b ** 2


def find_cushion(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    cushion_x = (x1 + x2) / 2
    cushion_y = (y1 + y2) / 2
    cushions = [[cushion_x, 0], [cushion_x, 130], [0, cushion_y], [260, cushion_y]]
    return cushions


def find_point(target, goal):
    x1, y1 = target[0], target[1]
    x2, y2 = goal[0], goal[1]
    distance = point_distance(target, goal)
    point_dis = distance + 5.73
    point_x = abs(x2 - x1) * point_dis / distance
    point_y = abs(y2 - y1) * point_dis / distance
    if goal[1] == 127:
        point_y = y2 - point_y
    else:
        point_y = point_y
    if goal[0] < target[0]:
        point_x = abs(x2 + point_x)
    else:
        point_x = abs(x2 - point_x)
    return [point_x, point_y]


def find_angle(white, point):
    x1, y1 = white[0], white[1]
    x2, y2 = point[0], point[1]
    degree = math.degrees(math.atan2(x2 - x1, y2 - y1))
    return degree


player = 1
goals = [[0, 0], [0, 127], [254, 0], [0, 127], [127, 127], [254, 127]]
balls = [[50, 50], [0, 0], [0, 0], [0, 0], [0, 0], [30, 30]]

if player == 1:
    white = balls[0]
    target_balls = [balls[1], balls[3]]
    op_balls = [balls[2], balls[4], balls[5]]
    black_ball = balls[5]
else:
    white = balls[0]
    target_balls = [balls[2], balls[4]]
    op_balls = [balls[1], balls[3], balls[5]]
    black_ball = balls[5]

result_point = []
for goal in goals:
    for target in target_balls:
        if target[0] != 0 or target[1] != 0:
            break
    else:
        target = black_ball
        point = find_point(black_ball, goal)
        if is_in_range(white, point, goal):
            for op_ball in op_balls:
                if op_ball[0] == 0 and op_ball[1] == 0: continue
                if point_line_distance(white, point, op_ball):
                    break
                if point_line_distance(target, goal, op_ball):
                    break
                result_point = point
                break
        if result_point: break

    for target in target_balls:
        if target[0] == 0 and target[1] == 0: continue
        point = find_point(target, goal)
        if is_in_range(white, point, goal):
            for op_ball in op_balls:
                if op_ball[0] == 0 and op_ball[1] == 0: continue
                if point_line_distance(white, point, op_ball):
                    break
                if point_line_distance(target, goal, op_ball):
                    break
                result_point = point
                break
        if result_point: break
    if result_point: break

if not result_point:
    for goal in goals:
        for target in target_balls:
            if target[0] != 0 or target[1] != 0: break
        else:
            target = black_ball
            point = find_point(target, goal)
            cushions = find_cushion(white, target)
            for cushion in cushions:
                if is_in_range(cushion, target, goal):
                    for op_ball in op_balls:
                        if op_ball[0] == 0 and op_ball[1] == 0: continue
                        if point_line_distance(white, cushion, op_ball): break
                        if point_line_distance(cushion, point, op_ball): break
                        if point_line_distance(target, goal, op_ball): break
                        result_point = point
                        break
                if result_point: break

        for target in target_balls:
            if target[0] == 0 and target[1] == 0: continue
            point = find_point(target, goal)
            cushions = find_cushion(white, point)
            for cushion in cushions:
                if is_in_range(cushion, target, goal):
                    for op_ball in op_balls:
                        if op_ball[0] == 0 and op_ball[1] == 0: continue
                        if point_line_distance(white, cushion, op_ball): break
                        if point_line_distance(cushion, point, op_ball): break
                        if point_line_distance(target, goal, op_ball): break
                        result_point = point
                        break
                if result_point: break
            if result_point: break
        if result_point: break

if not result_point:
    angle = find_angle(white, black_ball)
else:
    angle = find_angle(white, result_point)

if angle < 0:
    angle = 360 + angle

print(f'white : {white}')
print(f'target : {target} , goal : {goal}')
print(f'point : {result_point}')
print(f'angle : {angle}')
