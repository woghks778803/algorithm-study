# 실버2
# 상자넣기
N = int(input())
T = [int(i) for i in input().split()]
DP = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if T[i] > T[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))
"""
8
1 6 2 5 7 3 5 6

10
1 2 3 4 5 6 7 8 9 10

10
1 4 2 1 4 2 1 4 1 4

6
1 2 1 10 4 5
"""