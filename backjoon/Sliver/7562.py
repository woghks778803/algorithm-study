# 실버2
# 나이트의 이동
from collections import deque
T = int(input())
knight_x = [-2, -1, 1, 2, 2, 1, -1, -2]
knight_y = [1, 2, 2, 1, -1, -2, -2, -1]
result = []

# bfs 알고리즘
def bfs(start_x, start_y, end_x, end_y):
    # 방문 영역
    visit_chess = [[False for _ in range(I)] for _ in range(I)]
    # 시작점부터 현재까지 이동 횟수 저장
    depth = [[0 for _ in range(I)] for _ in range(I)]
    # 도착지 도달 여부
    loop_pass = False
    # 시작 값 방문 체크
    visit_chess[start_x][start_y] = True

    deq = deque()
    deq.append([start_x, start_y])
    while len(deq) > 0:
        x, y = deq.popleft()

        for i in range(len(knight_x)):
            mx = x+knight_x[i]
            my = y+knight_y[i]
            # 방문하지 않은 갈 수 있는 영역 체크
            if I > mx >= 0 and I > my >= 0 and visit_chess[mx][my] == False:
                visit_chess[mx][my] = True
                deq.append([mx, my])
                depth[mx][my] = depth[x][y]+1
                if mx == end_x and my == end_y:
                    # 도착지 도달
                    loop_pass = True
                    result.append(depth[mx][my])
                    break

        if loop_pass: break

for _ in range(T):
    I = int(input())

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    if start_x == end_x and start_y == end_y:
        # 시작점과 도착점이 같을 경우
        result.append(0)
    else:
        bfs(start_x, start_y, end_x, end_y)

# 테스트 케이스 결과 순차 출력
for i in result: print(i)

"""
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
"""