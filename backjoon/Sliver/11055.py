# 실버2
# 가장 큰 증가 부분 수열
N = int(input())
T = [int(i) for i in input().split()]
DP = T.copy()

for i in range(N):
    for j in range(i):
        if T[i] > T[j]: DP[i] = max(DP[i], DP[j] + T[i])

print(max(DP))
print(DP)

"""
10
1 100 2 50 60 3 5 6 7 8
"""