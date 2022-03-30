# 실버5
# 투자의 귀재 배주형
from math import floor

H, Y = map(int, input().split())
move = [[1, 1.05], [3, 1.2], [5, 1.35]]
DP = [0 for _ in range(Y+1)]
DP[0] = H

for i in range(1, Y+1):
    for m in move:
        if H >= i-m[0] >= 0:
            chk_money = floor(DP[i-m[0]]*m[1])
            DP[i] = max(chk_money, DP[i])

print(DP[Y])