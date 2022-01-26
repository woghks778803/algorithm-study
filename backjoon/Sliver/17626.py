# 실버4
# Four Squares
import math
N = int(input())
DP = [100000 for _ in range(50001)]
DP[0] = 0

for i in range(1, N+1):
    for j in range(1, int(math.sqrt(i))+1):
        if i == j**2:
            DP[i] = 1
            break
        else:
            DP[i] = min(DP[i], DP[i-j**2]+1)

print(DP[N])
