# 실버1
# 곱셈
import sys
a, b, c = map(int, sys.stdin.readline().split())
print(pow(a, b, c))

def my_pow(a,b,c):
    if b == 1:
        return a%c
    else:
        p = my_pow(a,b//2,c)
        if b%2 == 0:
            return p*p%c
        else:
            return p*p*a%c
print(my_pow(a,b,c))

#2147483647
"""
* 왜 %c을 붙여도 동일한 값이 나오는가

A = C * Q1 + R1 이때 0 ≤ R1 < C 이고 Q1는 정수이다. A mod C = R1

B = C * Q2 + R2 이때 0 ≤ R2 < C이고 Q2 는 정수이다. B mod C = R2

LHS = (A * B) mod C

LHS = ((C * Q1 + R1 ) * (C * Q2 + R2) ) mod C

LHS = (C * C * Q1 * Q2 + C * Q1 * R2 + C * Q2 * R1 + R1 * R 2 ) mod C

LHS = (C * (C * Q1 * Q2 + Q1 * R2 + Q2 * R1) + R1 * R 2 ) mod C

mod C로 정리하면 C의 배수 제거하기 때문에 마지막에 넣든 최초부터 계속 넣든 값은 같다

"""