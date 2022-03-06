# 골드4
# 색상환
def solve(n):
    sum_num = 0
    for i in range(1, n+1): sum_num += i
    
    return (sum_num+n)%1000000003

N = int(input())
K = int(input())

DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(4, N+1):
    DP[i][1] = i
    DP[i][2] = solve(i-3)

for i in range(6, N+1):
    for j in range(3, N+1):
        DP[i][j] = (DP[i-1][j] + DP[i-2][j-1])%1000000003

print(DP[N][K])
# print(DP)

"""

"""