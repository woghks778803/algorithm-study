# 실버5
# 타일 장식물
N = int(input())
DP = [0 for _ in range(81)]
DP[1] = 1
DP[2] = 1

for i in range(3, 81):
    DP[i] = DP[i-2] + DP[i-1]

print((DP[N-1]+DP[N]+DP[N])*2)