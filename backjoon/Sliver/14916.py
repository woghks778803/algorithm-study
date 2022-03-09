# 실버5
# 거스름돈
N = int(input())
DP = [int(1e9) for _ in range(100001)]
DP[2] = 1
DP[4] = 2
DP[5] = 1

for i in range(6, 100001):
    DP[i] = min(DP[i-5]+1, DP[i-2]+1)

if DP[N] == int(1e9): print(-1)
else: print(DP[N])
