# 실버1
# 이동하기
def dfs(x, y):
    if y < 0 or x < 0: return 0
    if DP[y][x] != -1: 
        pass
    else:
        DP[y][x] = T[y][x] + max(dfs(x-1, y), dfs(x, y-1))
    return DP[y][x]

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6) # 백준 런타임에러
    input = sys.stdin.readline
    N, M = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    DP = [[-1 for _ in range(M)] for _ in range(N)]

    dfs(M-1, N-1)
    print(DP[-1][-1])
    print(T)
    print(DP)

"""
3 4
1 2 3 4
0 0 0 5
9 8 7 6

3 3
1 0 0
0 1 0
0 0 1

4 3
1 2 3
6 5 4
7 8 9
12 11 10

2 2
0 0
0 3
"""