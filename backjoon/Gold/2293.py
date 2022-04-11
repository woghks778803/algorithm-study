# 골드5
# 동전 1
# X
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
T = []
for i in range(N):
    x = int(input())
    if x <= K: T.append(x)

real_n = len(T)
if real_n == 0:
    print(0)
else:
    DP = [0 for _ in range(K)]
    for i in range(real_n):

        DP[T[i]-1] += 1

        for j in range(T[i], K): DP[j] += DP[j-T[i]]

    print(DP[K-1])

"""
3 10
1
2
5
"""