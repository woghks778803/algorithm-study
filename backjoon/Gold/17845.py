# 골드5
# 수강 과목
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
DP = [[0 for _ in range(N+1)] for _ in range(K)]

for i in range(K):
    important, time = map(int, input().split())

    for j in range(1, N+1):
        if j < time:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max( DP[i-1][j], DP[i-1][j-time] + important )

print(DP[-1][-1])
# print(DP)

"""
80 3
650 40
700 60
60 40

26 6
10 4
11 5
12 6
13 7
14 8
16 9
"""