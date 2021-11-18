# 실버2
# 베르트랑 공준
import sys

INF = (123456*2)+1
PN = [True for _ in range(INF)]
PN[0] = False
PN[1] = False

for i in range(2, INF):
    if not PN[i]: continue
    for j in range(i*2, INF, i):
        PN[j] = False

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    result = 0
    for i in range(N+1, (N*2)+1):
        if PN[i]:
            result += 1
    print(result)

"""
1
10
13
100
1000
10000
100000
0
"""