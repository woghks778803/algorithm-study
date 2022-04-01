# 실버3
# 달나라 토끼를 위한 구매대금 지불 도우미
N = int(input())
DP = [100000 for _ in range(N+1)]
DP[0] = 0
T = [1, 2, 5, 7]

for t in T:
    if N >= t: DP[t] = 1

for i in range(N+1):
    for t in T:
        if N >= i-t >= 0:
            DP[i] = min(DP[i], DP[i-t]+1)

print(DP[N])
print(DP)
