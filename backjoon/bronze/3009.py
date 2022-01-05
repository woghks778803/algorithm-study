# 브론즈3
# 네 번째 점
x_point = [0, 1001]
y_point = [0, 1001]

input_points = []
for _ in range(3):
    x, y = map(int, input().split())
    if x > x_point[0]: x_point[0] = x
    if x < x_point[1]: x_point[1] = x
    if y > y_point[0]: y_point[0] = y
    if y < y_point[1]: y_point[1] = y
    input_points.append([x, y])

all_points = []
for x in x_point:
    for y in y_point:
        all_points.append([x, y])

for point in input_points: all_points.remove(point)

print(all_points[0][0], all_points[0][1])

"""
5 5
5 7
7 5

30 20
10 10
10 20
"""