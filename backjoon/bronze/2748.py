# 브론즈 1
# 피보나치 수 2
N = int(input())
DP = [0 for _ in range(N+1)]
DP[1] = 1

for i in range(2, N+1):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[N])