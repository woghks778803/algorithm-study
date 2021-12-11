# 실버1
# 미로 탐색
from collections import deque
N, M = map(int, input().split())
T = [list(map(int, input())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
depth = [[0 for _ in range(M)] for _ in range(N)]

def bfs():
    deq = deque()
    loop_check = False
    move_x = [0, 0, -1, 1]
    move_y = [-1, 1, 0, 0]
    visit[0][0] = True
    depth[0][0] = 1
    deq.append([0, 0])

    while len(deq) > 0:
        y, x = deq.popleft()

        for i in range(len(move_x)):
            next_x = move_x[i]+x
            next_y = move_y[i]+y

            if N > next_y >= 0 and M > next_x >= 0 and T[next_y][next_x] == 1 and visit[next_y][next_x] == False:
                visit[next_y][next_x] = True
                depth[next_y][next_x] = depth[y][x]+1
                deq.append([next_y, next_x])

                if next_x == M-1 and next_y == N-1:
                    loop_check = True
                    print(depth[N-1][M-1])
                    break
        
        if loop_check: break
    
bfs()




"""
2 2
11
11

4 6
101111
101010
101011
111011

4 6
110110
110110
111111
111101

2 25
1011101110111011101110111
1110111011101110111011101
"""