# 실버3
# 2×n 타일링 2
N = int(input())
INF = 10007
DP = [[0]*2 for _ in range(1001)]
DP[1][0] = DP[2][0] = 1
DP[1][1] = 0
DP[2][1] = 2

for i in range(3, 1001):
    DP[i][0] = sum(DP[i-1]) % INF
    DP[i][1] = DP[i-1][0]*2 % INF

print(sum(DP[N]) % INF)
