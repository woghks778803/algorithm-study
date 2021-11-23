# 실버3
# 링
N = int(input())
T = list(map(int, input().split()))

def GCD(b, s):
    gcd = 1
    for i in range(s+1, 1, -1):
        if b%i == 0 and s%i == 0:
            gcd=i
            break
    return gcd
    
for i in range(1, N):
    if T[0] > T[i]: gcd = GCD(T[0], T[i])
    else: gcd = GCD(T[i], T[0])
    print(str(T[0]//gcd)+"/"+str(T[i]//gcd))

"""
3
8 4 2

4
12 3 8 4

4
300 1 1 300

3
30 1 300
"""