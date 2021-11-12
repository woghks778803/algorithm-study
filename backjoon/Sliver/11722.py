# 실버2
# 가장 긴 감소하는 부분 수열
N = int(input())
T = list(map(int, input().split()))

DP = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if T[i] < T[j]:
            DP[i] = max(DP[j]+1, DP[i])

print(max(DP))

"""
6
10 30 10 20 20 10
"""