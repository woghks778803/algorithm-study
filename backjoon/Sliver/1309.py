# 실버1
# 동물원
N = int(input())
DP = [0 for _ in range(100001)]
DP[1] = 3
DP[2] = 7

for i in range(3, N+1):
    DP[i] = (DP[i-2] + DP[i-1]*2)%9901

print(DP[N])

"""
힌트
DP[1] = 1+2
DP[2] = 1+4+2
DP[3] = 1+6+8+2
DP[4] = 1+8+18+12+2
DP[5] = 1+10+32+38+16+2
"""
