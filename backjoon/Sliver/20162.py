# 실버2
# 간식 파티
import sys
input = sys.stdin.readline
N = int(input())
T = [int(input()) for _ in range(N)]
DP = [i for i in T]

for i in range(N):
    for j in range(i):
        if T[i] > T[j]:
            DP[i] = max(DP[i], DP[j]+T[i])

print(max(DP))


"""
5
4
5
1
2
3

10
3
7
3
4
8
5
10
9
3
4
"""