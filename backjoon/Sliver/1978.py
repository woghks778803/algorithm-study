# 실버4
# 소수 찾기
N = int(input())
T = list(map(int, input().split()))
PN = [True for _ in range(1001)]
PN[0] = False
PN[1] = False
for i in range(2, 1001):
    if not PN[i]: continue
    for j in range(i*2, 1001, i):
        PN[j] = False

result = 0
for i in T:
    if PN[i]: result += 1 

print(result)
"""
4
1 3 5 7
"""