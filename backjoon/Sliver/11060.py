# 실버2
# 점프 점프
def solve():
    for i in range(N):
        for j in range(1, T[i]+1):
            if N > i+j >= 0:
                DP[i+j] = min(DP[i+j], DP[i]+1)
            else:
                break

    if DP[-1] == INF: print(-1)
    else: print(DP[-1])

if __name__ == "__main__":
    INF = int(1e9)
    N = int(input())
    T = [int(i) for i in input().split()]
    DP = [INF for _ in range(N)]
    DP[0] = 0

    solve()

"""
10
1 2 0 1 3 2 1 5 4 2

11
1 2 1 1 3 0 0 1 1 1 1
"""