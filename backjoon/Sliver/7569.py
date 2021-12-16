# 실버1
# 토마토
import sys
from collections import deque
N, M, H = map(int, sys.stdin.readline().split())

T = [[list(map(int, sys.stdin.readline().split())) for _ in range(M)] for _ in range(H)]
depth = [[[0 for _ in range(N)] for _ in range(M)] for _ in range(H)]

# bfs 알고리즘
def bfs():
    move_x = [0, 0, 1, -1, 0, 0]
    move_y = [1, -1, 0, 0, 0, 0]
    move_z = [0, 0, 0, 0, 1, -1]
    deq = deque()
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if T[i][j][k] == 1: deq.append([k, j, i])

    while len(deq) > 0:
        x, y, z = deq.popleft()
        for i in range(len(move_x)):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            next_z = z + move_z[i]
            if N > next_x >= 0 and M > next_y >= 0 and H > next_z >= 0 and T[next_z][next_y][next_x] == 0:
                deq.append([next_x, next_y, next_z])
                T[next_z][next_y][next_x] = 1
                depth[next_z][next_y][next_x] = depth[z][y][x] + 1
    # print(T)
    # print(depth)

bfs()
max_value = 0
zero_check = False
for i in range(H):
    for j in range(M):
        if 0 in T[i][j]: 
            print(-1)
            zero_check = True
            break

        for k in range(N):
            if depth[i][j][k] > max_value: max_value = depth[i][j][k]

    if zero_check: break

if not zero_check: print(max_value)


"""
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
"""