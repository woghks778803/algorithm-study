# 실버1
# 토마토
from collections import deque
N, M = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(M)]
depth = [[0 for _ in range(N)] for _ in range(M)]

def bfs():
    move_x = [0, 0, 1, -1]
    move_y = [1, -1, 0, 0]
    deq = deque()

    # 첫 deqth에 해당하는 위치를 먼저 저장
    for y in range(M):
        for x in range(N):
            if T[y][x] == 1: deq.append([x, y])

    while len(deq) > 0:
        x, y = deq.popleft()

        for i in range(len(move_x)):
            next_x = move_x[i] + x
            next_y = move_y[i] + y
            if N > next_x >= 0 and M > next_y >= 0 and T[next_y][next_x] == 0:
                depth[next_y][next_x] = depth[y][x] + 1
                T[next_y][next_x] = 1
                deq.append([next_x, next_y])

bfs()
zero_check = False
max_depth = 0
for y in range(M):
    if 0 in T[y]:
        zero_check = True
        break

    for x in range(N):
        if depth[y][x] > max_depth: max_depth = depth[y][x]

if zero_check: print(-1)
else: print(max_depth)

print(T)
print(depth)
"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0

2 2
1 -1
-1 1
"""