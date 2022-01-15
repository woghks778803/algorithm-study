# 실버2
# 1, 2, 3 더하기 3
N = int(input())
INF = 1000000009

DP = [0 for _ in range(1000001)]
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4, 1000001): DP[i] = (DP[i-1] + DP[i-2] + DP[i-3])%INF

for _ in range(N): print(DP[int(input())])

"""
3
4
7
10
"""