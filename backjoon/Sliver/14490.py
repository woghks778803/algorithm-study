# 실버4
# 백대열
# 유클리드 호제법
def uc(b, s):
    while b%s != 0:
        temp = b%s
        b = s
        s = temp
    
    return s

n, m = map(int, input().split(":"))
if m > n: gcd = uc(m, n)
else: gcd = uc(n, m)

print(str(n//gcd)+":"+str(m//gcd))

"""
100:10
18:24
"""
