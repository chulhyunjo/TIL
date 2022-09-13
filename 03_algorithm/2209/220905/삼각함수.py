import math


def points_distance(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result


def find_point(target, goal):
    x1, y1 = target[0], target[1]
    x2, y2 = goal[0], goal[1]
    distance = points_distance(target, goal)
    result_distance = distance + 5.73
    point_x = abs(x2 - abs(x1 - x2) * result_distance / distance)
    point_y = abs(y2 - abs(y1 - y2) * result_distance / distance)
    return [point_x, point_y]


def find_angle(white, point):
    x1, y1 = white[0], white[1]
    x2, y2 = point[0], point[1]
    degree = math.degrees(math.atan2(x2 - x1, y2 - y1))
    return degree


def find_cushions(white, point):
    x1, y1 = white[0], white[1]
    x2, y2 = point[0], point[1]
    cushions_x = (x1 + x2) / 2
    cushions_y = (y1 + y2) / 2
    cushion_x = [[cushions_x, 0], [cushions_x, 130], ]
    cushion_y = [[0, cushions_y], [260, cushions_y]]
    result = []
    for cushion in cushion_x:
        if 0 < cushion[0] < 3 or 127 < cushion[0] < 133 or 255 < cushion[0] < 260:
            continue
        result.append(cushion)
    for cushion in cushion_y:
        if 0 < cushion[1] < 3 or 125 < cushion[1] < 130:
            continue
        result.append(cushion)


def check_range(point1, point2, goal):
    a = points_distance(point1, point2)
    b = points_distance(point2, goal)
    c = points_distance(point1, goal)
    return c ** 2 > a ** 2 + b ** 2


def check_line(point1, point2, op):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    a, b = op[0], op[1]
    area = abs((x2 - a) * (y1 - b) - (x1 - a) * (y2 - b))
    dis = points_distance(point1, point2)
    result = area / dis
    if x1 > x2 : x1, x2 = x2, x1
    if y1 > y2 : y1, y2 = y2, y1
    if x1 < a < x2 and y1 < b < y2:
        return result <= 5.73
    else:
        return False
