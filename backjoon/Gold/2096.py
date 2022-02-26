# 골드4
# 내려가기
import sys
import copy
input = sys.stdin.readline
N = int(input())
T = [[int(i) for i in input().split()] for _ in range(N)]
MAX_DP = [[0 for _ in range(3)] for _ in range(2)]
MAX_DP[0][0] = T[0][0]
MAX_DP[0][1] = T[0][1]
MAX_DP[0][2] = T[0][2]
MIN_DP = copy.deepcopy(MAX_DP)

for i in range(1, N):
    for j in range(3):
        if j == 0:
            MAX_DP[1][j] = max(T[i][j] + MAX_DP[0][j], T[i][j] + MAX_DP[0][j+1])
            MIN_DP[1][j] = min(T[i][j] + MIN_DP[0][j], T[i][j] + MIN_DP[0][j+1])
        elif j == 1:
            MAX_DP[1][j] = max(T[i][j] + MAX_DP[0][j-1], T[i][j] + MAX_DP[0][j], T[i][j] + MAX_DP[0][j+1])
            MIN_DP[1][j] = min(T[i][j] + MIN_DP[0][j-1], T[i][j] + MIN_DP[0][j], T[i][j] + MIN_DP[0][j+1])
        elif j == 2:
            MAX_DP[1][j] = max(T[i][j] + MAX_DP[0][j-1], T[i][j] + MAX_DP[0][j])
            MIN_DP[1][j] = min(T[i][j] + MIN_DP[0][j-1], T[i][j] + MIN_DP[0][j])

    MAX_DP[0] = MAX_DP[1].copy()
    MIN_DP[0] = MIN_DP[1].copy()

print(max(MAX_DP[0]), min(MIN_DP[0]))
print(MAX_DP, MIN_DP)

"""
3
1 2 3
4 5 6
4 9 0

3
0 0 0
0 0 0
0 0 0
"""