# 실버3
# 피보나치 수의 확장
N = int(input())
INF = int(1e9)
DP = [0 for _ in range(1000001)]
DP[1] = 1

for i in range(2, 1000001):
    if DP[i-2] >= DP[i-1]:
        DP[i] = (DP[i-2] - DP[i-1])%INF
    else:
        DP[i] = (abs(DP[i-2] - DP[i-1])%INF)*-1

if N > 0:
    print(1)
else:
    N = abs(N)
    if DP[N] > 0:
        print(1)
    elif DP[N] < 0:
        print(-1)
    else:
        print(0)

print(abs(DP[N]))
# print(DP)

# n ≤ 1 일 경우 f(n-2) = f(n)-f(n-1) f(-1) = f(1)-f(0) 
# n > 1 일 경우 f(n) = f(n-1)+f(n-2)