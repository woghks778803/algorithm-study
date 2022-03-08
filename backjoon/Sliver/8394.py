# 실버4
# 악수
N = int(input())
DP = [1, 2]

for i in range(2, N):
    temp = DP[0]
    DP[0] = DP[1]
    DP[1] = (DP[0] + temp)%10

if N == 1:
    print(DP[0])
else:
    print(DP[-1])

