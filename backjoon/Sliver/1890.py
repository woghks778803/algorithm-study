# 실버2
# 점프 
def in_scope(x, y):
    if 0 <= x < N and 0 <= y < N: return True
    else: return False

def dfs(x, y):
    if x == N-1 and y == N-1: return 1

    if DP[x][y] == -1:
        DP[x][y] = 0
        for i in range(2):
            next_x = x
            next_y = y
            if i == 0: next_x += T[x][y]
            else: next_y += T[x][y]
            
            if in_scope(next_x, next_y):
                DP[x][y] += dfs(next_x, next_y)

    return DP[x][y]

if __name__ == "__main__":
    N = int(input())
    T = [[int(i) for i in input().split()] for _ in range(N)]

    DP = [[-1 for _ in range(N)] for _ in range(N)]

    print(dfs(0, 0))
    for i in DP: print(i)

"""
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0

4
1 2 2 3
1 1 3 3
3 1 1 3
3 2 1 0

4
1 2 2 3
1 1 3 3
3 1 0 3
3 2 1 0

9
3 1 2 2 3 3 1 1 2
1 1 2 1 1 2 3 1 2
2 1 1 3 2 2 1 3 1
3 3 1 1 1 3 1 2 1
3 2 2 2 1 1 3 3 1
3 1 3 2 2 3 1 3 3
3 1 1 2 1 1 1 1 1
2 3 1 3 1 3 2 2 2
3 3 3 2 3 1 3 3 0
= 3 2 3 2 3 3
= 3 2 3 2 1 1 1 3
= 3 2 3 3 1 1 3
= 3 3 1 1 1 1 3 3
= 3 3 1 2 1 3 3

4
1 3 0 0
1 0 0 0
1 0 0 0
1 1 0 0
"""