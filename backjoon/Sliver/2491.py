# 실버3
# 수열
N = int(input())
T = [int(i) for i in input().split()]
S_DP = [1 for _ in range(N)]
L_DP = [1 for _ in range(N)]

for i in range(1, N):
    if T[i] >= T[i-1]:
        L_DP[i] = max(L_DP[i], L_DP[i-1]+1)
    if T[i] <= T[i-1]:
        S_DP[i] = max(S_DP[i], S_DP[i-1]+1)

print( max(max(S_DP), max(L_DP)) )
print(S_DP, L_DP)

"""
9
1 2 2 4 4 5 7 7 2

9
4 1 3 3 2 2 9 2 3

11
1 5 3 6 4 7 1 3 2 9 5
"""