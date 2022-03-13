# 실버3
# 피보나치 비스무리한 수열
N = int(input())
DP = [0 for _ in range(117)]
DP[1] = DP[2] = DP[3] = 1

for i in range(4, N+1):
    DP[i] = DP[i-1] + DP[i-3]
print(DP[N])