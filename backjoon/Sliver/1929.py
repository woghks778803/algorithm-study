# 실버2
# 소수 구하기
import sys
M, N = map(int, sys.stdin.readline().split())

PN = [True for _ in range(N+1)]
PN[0] = False
PN[1] = False
# 공식 - 에라토스테네스의 체
for i in range(2, N+1):
    if not PN[i]: continue
    for j in range(i*2, N+1, i):
        PN[j] = False

for i in range(M, N+1):
    if PN[i]: sys.stdout.write(str(i)+"\n")
