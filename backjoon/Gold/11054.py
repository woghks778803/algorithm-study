# 골드3
# 가장 긴 바이토닉 부분 수열
N = int(input())
T = list(map(int, input().split()))
DP = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if T[j] < T[i]: 
            DP[i] = max(DP[j]+1, DP[i])

for i in range(1, N):
    for j in range(i):
        if T[j] > T[i]: 
            DP[i] = max(DP[j]+1, DP[i])

print(max(DP))
"""
10
1 5 2 1 4 3 4 5 2 1

12
1 3 2 5 6 5 4 7 3 2 1 1
"""