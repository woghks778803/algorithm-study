# 실버5
# 다리놓기
import sys
test_case_count = int(sys.stdin.readline().strip())

def factorial(n):
    r = 1
    for i in range(1,n+1): r *= i
    return r

for i in range(test_case_count):
    N, M = map(int, sys.stdin.readline().split())
    print(int(factorial(M) / (factorial(M-N) * factorial(N))))

# 경우의 수
# 조합(순서x) = n!/(n-r)!r!
# 순열(순서o) = n!/(n-r)!
"""
반례
3
2 2
1 5
13 29
"""