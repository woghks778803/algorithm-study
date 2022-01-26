# 실버1
# 스티커
T = int(input())
for _ in range(T):
    N = int(input())
    lst = [[int(i) for i in input().split()] for _ in range(2)]
    DP = [[0 for _ in range(N)] for _ in range(2)]
    if N > 1:
        DP[0][0] = lst[0][0]
        DP[1][0] = lst[1][0]
        DP[0][1] = DP[1][0] + lst[0][1]
        DP[1][1] = DP[0][0] + lst[1][1]

        for i in range(2, N):
            DP[0][i] = max(DP[1][i-2], DP[1][i-1]) + lst[0][i]
            DP[1][i] = max(DP[0][i-2], DP[0][i-1]) + lst[1][i]

        print(max(DP[0][-1], DP[1][-1]))
    else:
        print(max(lst[0][0], lst[1][0]))

    print(lst)
    print(DP)
"""
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
"""