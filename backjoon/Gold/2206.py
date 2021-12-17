# 골드4
# 벽 부수고 이동하기
from collections import deque
N, M = map(int, input().split())
T = [list(map(int, input())) for _ in range(N)]
visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]
loop_check = False

# bfs 알고리즘
def bfs():
    deq = deque()
    deq.append([0, 0, 0])
    global loop_check
    while len(deq) > 0:
        x, y, wall = deq.popleft()

        for i in range(len(move_x)):
            next_x = x+move_x[i]
            next_y = y+move_y[i]
            if N > next_y >= 0 and M > next_x >= 0 and visit[wall][next_y][next_x] == 0:
                if T[next_y][next_x] == 1:
                    if wall == 0:
                        deq.append([next_x, next_y, 1])
                        visit[1][next_y][next_x] = visit[0][y][x] + 1
                        if next_x == M-1 and next_y == N-1: loop_check = True
                else:
                    deq.append([next_x, next_y, wall])
                    visit[wall][next_y][next_x] = visit[wall][y][x] + 1
                    if next_x == M-1 and next_y == N-1: loop_check = True

bfs()
if N == 1 and M == 1: 
    print(1)
else:
    if loop_check:
        wall0 = visit[0][N-1][M-1]
        wall1 = visit[1][N-1][M-1]

        if wall0 != 0 and (wall0 < wall1 or wall1 == 0):
            print(wall0+1)
        elif wall1 != 0:
            print(wall1+1)
    else: 
        print(-1)

print(visit)


"""
6 4
0100
1110
1000
0000
0111
0000

4 4
0111
1111
1111
1110

2 2
01
10

6 5
01000
10000
00000
00000
00001
00010

6 5
01000
10000
11110
00000
01111
00000

6 5
01000
00000
11110
00000
01111
00000

1 1
0

13 13
0100011011000
0001001010000
0000100001000
1100010101011
1111101111000
1011010001001
0100001001001
0100111010001
0101010000100
0001110100000
0000001000100
1010001000111
1001000100000
"""