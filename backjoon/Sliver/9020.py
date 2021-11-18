# 실버1
# 골드바흐의 추측
import sys
N = int(sys.stdin.readline())

PN = [True for i in range(10001)]
PN[0] = False
PN[1] = False
for i in range(2, int(10001**0.5)+1):
    if not PN[i]: continue
    for j in range(i*2, 10001, i):
        PN[j] = False

for i in range(N):
    T = int(sys.stdin.readline())
    for j in range(T//2, 1, -1):
        if PN[j] and PN[T-j]:
            print(j, T-j)
            break


"""
10
8
10
16
12
1000
5000
2500
10000
1200
4
"""