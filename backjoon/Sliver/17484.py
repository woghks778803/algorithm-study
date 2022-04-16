# 실버4
# 진우의 달 여행 (Small)
from collections import deque

def bfs(p):
    move = [-1, 0, 1]
    dq = deque(p)

    while dq:
        x, y, position = dq.popleft()

        for m in move:
            next_x = x + 1
            next_y = y + m

            if M > next_y >= 0 and N > next_x >= 0:
                if position == None:
                    DP[m][next_x][next_y] = T[x][y] + T[next_x][next_y]
                elif position != m:
                    DP[m][next_x][next_y] = min(DP[m][next_x][next_y], DP[position][x][y] + T[next_x][next_y])

                dq.append([next_x, next_y, m])


N, M = map(int, input().split())
DP = [[[int(1e10) for _ in range(M)] for _ in range(N)] for _ in range(3)]
T = [[int(i) for i in input().split()] for _ in range(N)]

point = []
for i in range(M): 
    point.append([0, i, None])
    
bfs(point)
print(min([min(DP[i][-1]) for i in range(3)]))

# print(T)
# print(DP[0][-1])
# print(DP[1][-1])
# print(DP[2][-1])


"""
6 4
5 8 5 1
3 5 8 4
9 77 65 5
2 1 5 2
5 98 1 5
4 95 67 58
"""