# 실버4
# 터렛
import sys
import math
N = int(sys.stdin.readline().strip())
for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    Real = int(math.pow(abs(x2-x1),2) + math.pow(abs(y2-y1),2))
    R = int(math.pow(r1 + r2,2))

    if x1 == x2 and y1 == y2 and r1 != r2: # 위치가 같은데 거리가 다른경우
        print(0)
    elif x1 == x2 and y1 == y2 and r1 == r2: # 위치가 같은데 거리가 같은경우
        print(-1)
    elif R == Real: # a와 b의 거리와 (a와 c의 거리, a와 b의 거리의 합)이 같은경우
        print(1)
    elif R < Real: # a와 b의 거리보다 (a와 c의 거리, a와 b의 거리의 합)이 작을경우(이어질 수 없음)
        print(0)
    else:
        if r1 > r2:
            min = r2
            max = r1
        else:
            min = r1
            max = r2

        sqrt_real = math.sqrt(Real)

        if min+sqrt_real < max:
            print(0)
        elif min+sqrt_real == max:
            print(1)
        elif min+sqrt_real > max:
            print(2)


"""
1
1 1 1 1 1 1

1
0 0 1 0 1 5

1
0 0 5 0 0 5

1
0 0 3000 4000 2500 2500
"""
        