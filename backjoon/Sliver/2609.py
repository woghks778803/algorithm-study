# 실버5
# 최대공약수와 최소공배수
N, M = map(int, input().split())

def GCD(b, s):
    gcd = 1
    for i in range(s+1, 1, -1):
        if s % i == 0 and b % i == 0:
            gcd = i
            break
    return gcd

if N > M: gcd = GCD(N, M)
else: gcd = GCD(M, N)

print(gcd)
print((N*M)//gcd)
"""
24 18
3 6                     3 6
1048 5760           8 754560
6 3                     3 6
9924 5545          1 55028580
77 66                 11 462
37 74                 37 74
1 1                    1 1
1 150                 1 150
150 1                 1 150
24 18                 6 72
7  7                   7 7
2131 87             1 185397
77 65                1 5005
153 71              1 10863
"""