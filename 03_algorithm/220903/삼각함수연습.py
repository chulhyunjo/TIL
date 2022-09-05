import math

def point_distance(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    one = x1 - x2
    two = y1 - y2
    result = math.sqrt(one**2 + two** 2)
    return result


def point_line_distance(point1, point2, op):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    a, b = op[0], op[1]
    area = abs((x1-a)*(y2-b) - (x2-a)*(y1-b))
    dis_p1_p2 = point_distance(point1,point2)
    result = area/dis_p1_p2
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    if x1<a<x2 and y1<b<y2:
        return result
    else:
        return 6


def find_point(goal, point2):
    x1, y1 = goal[0], goal[1]
    x2, y2 = point2[0] , point2[1]
    dis_g_p2 = point_distance(goal, point2)
    to_result = dis_g_p2 + 5.73
    result_x = abs(x1 - abs(x2-x1) * to_result / dis_g_p2)
    result_y = abs(y1 - abs(y2-y1) * to_result / dis_g_p2)
    return [result_x, result_y]


def is_in_degree(white, point, goal):
    c = point_distance(white, goal)
    b = point_distance(point, goal)
    a = point_distance(white, point)
    if c**2 > a**2 + b**2:
        return True
    else: return False

def angle_ans(white, finded_point):
    first = finded_point[1] - white[1]
    second = finded_point[0] - white[0]
    angle = math.degrees(math.atan2(second,first))
    return angle

def find_cusion(white, point):
    cusion_x = (white[0] + point[0]) / 2
    cusion_y = (white[1] + point[1]) / 2
    return [[cusion_x, 0], [cusion_x, 130], [0, cusion_y,], [260, cusion_y]]


ball = [7, 10]
goals = [[0,0], [100,0] ,[0,50],[50,0],[0,100], [100, 100]]
balls = [[0, 0],[10,30]]
op_balls = [[52,52],[35,34]]
result_goal = []
use_cusion = False
angle = 0
for ball2 in balls:
    if not ball2[0] and not ball2[1]: continue
    for goal in goals:
        point = find_point(goal, ball2)
        if is_in_degree(ball,point,goal):
            no = False
            for op_ball in op_balls:
                if point_line_distance(ball, point, op_ball) <= 5.73:
                    no = True
                    break
                if point_line_distance(ball2, goal, op_ball) <= 5.73:
                    no = True
                    break
            if not no:
                result_goal = goal
        if result_goal:
            break
    print(result_goal)
    if not result_goal:
        for goal in goals:
            point = find_point(goal, ball2)
            cusions = find_cusion(ball,point)
            for cusion in cusions:
                if is_in_degree(cusion,point,goal):
                    if point_line_distance(cusion, point, op_ball) <= 5.73:
                        continue
                    if point_line_distance(ball2, goal, op_ball) <= 5.73:
                        continue
                    result_goal = goal
                    use_cusion = True
                if result_goal:
                    break

    if use_cusion:
        angle = angle_ans(ball, cusion)
    else:
        angle = angle_ans(ball, point)
    if angle < 0:
        angle = 360 + angle
    if use_cusion:
        print(result_goal, angle, use_cusion,cusion, point)

    else: print(result_goal, angle, use_cusion, point)
    if angle: break