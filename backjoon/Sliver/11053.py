# 실버2
# 가장 긴 증가하는 부분 수열
# X
N = int(input())
T = list(map(int, input().split()))

DP = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if T[j] < T[i]:
            DP[i] = max(DP[j]+1, DP[i])

print(max(DP))




"""
반례

6
10 20 10 30 20 50

5
5 1 2 3 4

5
40 1 5 10 90

7
30 20 30 10 30 20 30

8
0 10 0 30 20 30 10 40
"""