# 실버4
# 피보나치 수 4
N = int(input())
DP = [0, 1]

for i in range(2, N+1):
    sum_dp = sum(DP)
    DP[0] = DP[1]
    DP[1] = sum_dp
    
if N == 0:
    print(DP[0])
else:
    print(DP[1])
    