# 브론즈2
# 트럭 주차
A, B, C = map(int, input().split())

T = [list(map(int, input().split())) for _ in range(3)]
DP = [0 for _ in range(100)]

for i in T:
    for j in range(i[0], i[1]): DP[j] += 1

result = 0
for i in range(100):
    if DP[i] == 1: result += A
    elif DP[i] == 2: result += B*2
    elif DP[i] == 3: result += C*3

print(result)

"""
5 3 1
1 6
3 5
2 8

10 8 6
15 30
25 50
70 80
"""