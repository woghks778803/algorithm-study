# 실버5
# BABBA 
K = int(input())
DP = [[0, 0] for _ in range(K+1)]
DP[0] = [1, 0]

for i in range(1, K+1):
    DP[i][0] = DP[i-1][1]
    DP[i][1] = sum(DP[i-1])

print(*DP[K])
# print(DP)