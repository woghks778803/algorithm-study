# 실버3
# Generations of Tribbles
N = int(input())
DP = [0 for _ in range(70)]
DP[0] = 1
DP[1] = 1
DP[2] = 2
DP[3] = 4
for i in range(4, 70): DP[i] = DP[i-1]+DP[i-2]+DP[i-3]+DP[i-4]
for i in range(N): print(DP[int(input())])