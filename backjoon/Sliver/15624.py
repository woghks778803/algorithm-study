# 실버4
# 피보나치 수 7
N = int(input())
DP = [0, 1, 1]

if N == 0:
    print(N)
else:
    for i in range(2, N):
        DP[0] = DP[1]
        DP[1] = DP[2]
        DP[2] = (DP[0]+DP[1])%1000000007

    print(DP[2])
