# 골드3
# 욕심쟁이 판다
def dfs(x, y):
    for m in move:
        next_x = x + m[0]
        next_y = y + m[1]

        if N > next_x >= 0 and N > next_y >= 0 and T[next_x][next_y] > T[x][y]:
            if not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                DP[x][y] = max(dfs(next_x, next_y)+1, DP[x][y])
            else:
                DP[x][y] = max(DP[next_x][next_y]+1, DP[x][y])

    return DP[x][y]

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6) # 백준 런타임에러
    N = int(input())
    T = [[int(i) for i in input().split()] for _ in range(N)]
    move = [[1,0], [-1,0], [0,1], [0,-1]]
    DP = [[1 for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)

    print( max([max(DP[i]) for i in range(N)]) )
    
"""
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8

4
5 6 7 8
4 11 10 9
5 12 1  16
8 13 14 15
"""