# 실버2
# 안녕
N = int(input())
health = 100
L = [int(i) for i in input().split()] # 체력
J = [int(i) for i in input().split()] # 기쁨
DP = [[0 for _ in range(health)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(health):
        if j-L[i-1] < 0: # 소모 체력값보다 j가 적을경우
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-L[i-1]] + J[i-1])

print(DP[-1][-1])

"""
3
1 21 79
20 30 25

1
100
20

8
100 15 1 2 3 4 6 5
49 40 1 2 3 4 5 4

8
100 26 13 17 24 33 100 99
34 56 21 1 24 34 100 99
"""