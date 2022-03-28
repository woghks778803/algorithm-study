# 실버5
# 파스칼의 삼각형
N, K = map(int, input().split())
DP = [[0 for _ in range(30)] for _ in range(30)]
for i in range(30):
    DP[i][0] = 1

for i in range(1, 30):
    for j in range(1, 30):
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j]

print(DP[N-1][K-1])