# 실버5
# 소수
M = int(input())
N = int(input())

PN = [True for _ in range(N+1)]
PN[0] = False
PN[1] = False
result = []

# 에라토스테네스의 체
for i in range(2, N+1):
    if not PN[i]: 
        continue
    else: 
        if N >= i >= M: result.append(i)

    for j in range(i*2, N+1, i): PN[j] = False

if not result:
    print(-1)
else:
    print(sum(result))
    print(min(result))

"""
60
100

64
65

64
67
"""