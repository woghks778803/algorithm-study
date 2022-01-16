# 실버2
# 1, 2, 3 더하기 5
import sys
INF = 1000000009
T = int(sys.stdin.readline())

dp = [[0]*4 for _ in range(100001)]
dp[1][1] = dp[2][2] = dp[3][3] = 1
dp[3][1] = dp[3][2] = 1

for i in range(4,100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % INF
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % INF
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % INF

for _ in range(T):
    n = int(sys.stdin.readline())
    sys.stdout.write(str(sum(dp[n])% INF)+'\n')


"""
3
4
7
10
"""