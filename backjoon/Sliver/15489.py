# 실버5
# 파스칼 삼각형
R, C, W = map(int, input().split())
DP = [[0 for _ in range(30)] for _ in range(30)]

for i in range(30): 
    DP[i][0] = 1
    
    for j in range(1, i+1):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-1]

result = 0
for r in range(R-1, (R-1)+W):
    c_scope = r-(R-1)

    for c in range(C-1, C+c_scope):
        result += DP[r][c]

print(result)
# print(DP)

"""
3 1 4
"""