# 부녀회장이 될테야
# 브론즈2
N = int(input())

for i in range(N):
    k = int(input())
    n = int(input())
    DP = [[0 for _ in range(n)] for _ in range(k+1)]

    for a in range(k+1): DP[a][0] = 1
    for b in range(n): DP[0][b] = b+1

    for a in range(1, k+1):
        for b in range(1, n):
            DP[a][b] = DP[a-1][b] + DP[a][b-1]
    
    print(DP[k][n-1])
    # print(DP)
    # print(k, n)

"""
2
1
3
2
3
"""