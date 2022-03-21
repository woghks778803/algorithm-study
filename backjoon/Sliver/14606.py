# 실버4
# 피자 (Small)
N = int(input())
DP = [0 for _ in range(N+1)]

if N == 1:
    print(0)
else:
    DP[2] = 1

    for i in range(3, N+1):
        if i%2 == 1:
            DP[i] = DP[i//2] + DP[i//2+1] + (i//2) * (i//2+1)
        else:
            DP[i] = DP[i//2] + DP[i//2] + (i//2)**2

    print(DP[N])
