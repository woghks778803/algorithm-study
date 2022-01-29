# 실버3
# 제곱수의 합
import math
N = int(input())
DP = [1000000 for _ in range(100001)]
DP[0] = 0

for i in range(1, N+1):
    for j in range(int(math.sqrt(i)), 0, -1):
        if i == j**2:
            DP[i] = 1
            break
        else:
            DP[i] = min(DP[i], DP[i-j**2]+1)

print(DP[N])