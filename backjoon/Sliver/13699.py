# 실버4
# 점화식
N = int(input())
DP = [0 for _ in range(36)]
DP[0] = 1

for i in range(1, N+1):
    for j in range(i):
        DP[i] += DP[j]*DP[i-j-1]

print(DP[N])