# 골드3
# 다리 만들기
from collections import deque

def diff_len(continent_num, continent_point):

    for continent_diff in range(cnt):
        if continent_num != continent_diff: # 같은 대륙 필터
            for point in range(len(continent[continent_diff])):
                diff_x = abs(continent_point[0] - continent[continent_diff][point][0])
                diff_y = abs(continent_point[1] - continent[continent_diff][point][1])
                diff = diff_x+diff_y-1

                global result
                if result > diff: result = diff


def in_scope(x, y):
    if N > x >= 0 and N > y >= 0: return True
    return False

def bfs(x, y):
    dq = deque([[x, y]])    

    while dq:
        x, y = dq.popleft()

        for m in move:
            next_x = x + m[0]
            next_y = y + m[1]

            if in_scope(next_x, next_y) and not in_visited[next_x][next_y] and T[next_x][next_y] == 1:
                in_visited[next_x][next_y] = True
                dq.append([next_x, next_y])

            if in_scope(next_x, next_y) and not border_visited[x][y] and T[next_x][next_y] == 0:
                border_visited[x][y] = True
                continent[cnt].append([x, y])

N = int(input())
T = [[int(i) for i in input().split()] for _ in range(N)]
DP = [[False for _ in range(N)] for _ in range(N)]
in_visited = [[False for _ in range(N)] for _ in range(N)]
border_visited = [[False for _ in range(N)] for _ in range(N)]
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
continent = []

cnt = 0
for i in range(N):
    for j in range(N):
        if not in_visited[i][j] and T[i][j] == 1:
            in_visited[i][j] = True
            continent.append([])
            bfs(i, j)
            cnt += 1

result = int(1e9)
for i in range(cnt):
    for j in range(len(continent[i])):
        diff_len(i, continent[i][j])

print(result)
# print(continent)


"""
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
"""