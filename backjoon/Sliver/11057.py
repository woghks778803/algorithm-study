# 실버1
# 오르막 수
N = int(input())
INF = 10007
DP = [[0 for _ in range(10)] for _ in range(1000)]
for i in range(10): DP[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0: DP[i][j] = sum(DP[i-1])%INF
        else: DP[i][j] = (DP[i][j-1] - DP[i-1][j-1])%INF

print(sum(DP[N-1])%INF)
# print(DP)


