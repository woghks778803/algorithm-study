# 실버4
# 연속부분최대곱
N = int(input())
T = [float(input()) for _ in range(N)]
DP = [0 for _ in range(N)]
DP[0] = T[0]

for i in range(1, N):
    DP[i] = max(T[i], DP[i-1]*T[i])
print(f"{max(DP):.3f}")

"""
8
1.1
0.7
1.3
0.9
1.4
0.8
0.7
1.4
"""