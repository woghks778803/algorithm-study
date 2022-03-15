# 실버3
# 돌 게임3
N = int(input())
if N >= 4: DP = [0 for _ in range(N+1)]
else: DP = [0 for _ in range(5)]
DP[1] = 1
DP[2] = 2
DP[3] = 1
DP[4] = 1

for i in range(5, N+1):
    if DP[i-4]==2 or DP[i-3]==2 or DP[i-1]==2:
        DP[i] = 1
    else:
        DP[i] = 2

if DP[N]%2 == 1: print("SK")
else: print("CY")
# print(DP[N])
print(DP)

