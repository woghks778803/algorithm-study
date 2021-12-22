# 실버3
# 2×n 타일링
# 이런 문제는 일단 1부터 차례대로 대입해서 규칙을 찾아보자..
N = int(input())
DP = [0 for _ in range(N+1)]

if N < 3:
    DP[N] = N
else:
    DP[1] = 1
    DP[2] = 2

    for i in range(3, N+1):
        DP[i] = (DP[i-1] + DP[i-2])%10007

print(DP[N])
