# 실버5
# 사과 담기 게임
N, M = map(int, input().split())
J = int(input())
cur_point = [1, M]

result = 0
for _ in range(J):
    fall_point = int(input())

    if cur_point[0] <= fall_point <= cur_point[1]:
        pass
    else:
        if abs(cur_point[0]-fall_point) < abs(cur_point[1]-fall_point):
            move = abs(cur_point[0]-fall_point)
            if cur_point[0] > fall_point:
                cur_point[0] -= move
                cur_point[1] -= move
            else:
                cur_point[0] += move
                cur_point[1] += move
        else:
            move = abs(cur_point[1]-fall_point)
            if cur_point[1] > fall_point:
                cur_point[0] -= move
                cur_point[1] -= move
            else:
                cur_point[0] += move
                cur_point[1] += move
            
        result += move

print(result)

"""
5 1
3
1
5
3

5 2
3
1
5
3
"""