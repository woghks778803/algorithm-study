# 실버1
# 안전 영역
def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()

        for i in move:
            next_x = x+i[0]
            next_y = y+i[1]

            if N > next_x >= 0 and N > next_y >= 0 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                dq.append([next_x, next_y])


if __name__ == "__main__":
    from collections import deque
    N = int(input())
    DP = [[int(i) for i in input().split()] for _ in range(N)]
    move = [[1,0], [-1,0], [0,1], [0,-1]]

    result = 0
    for h in range(101):
        cnt = 0
        visited = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if DP[i][j] <= h:
                    visited[i][j] = True

        for i in range(N):
            for j in range(N):
                if not visited[i][j]: 
                    cnt += 1
                    bfs(i, j)

        if cnt > result:
            result = cnt

    print(result)
    # print(visited)
    # print(DP)

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
"""