# 골드3
# 피보나치 수 6
import sys
sys.setrecursionlimit(10**6) # 백준 런타임에러
N = int(input())
INF = 1000000007

def my_pow(n):
    return (n*n)%INF

mat = {}
# 공식 - 도가뉴의 항등식
# a2n-1 = (an)2+(an-1)2
# a2n = an(an+2*an-1)
def fibonacci(n):

    if n <= 1:
        return n
    elif n % 2 == 1:
        if mat.get((n+1)//2): a = mat[(n+1)//2]
        else: a = fibonacci((n+1)//2)

        if mat.get((n+1)//2 -1): b = mat[(n+1)//2 -1]
        else: b = fibonacci((n+1)//2 -1)

        result = my_pow( a ) + my_pow( b )
    else:
        if mat.get(n//2): a = mat[n//2]
        else: a = fibonacci(n//2)

        if mat.get((n//2)-1): b = mat[(n//2)-1]
        else: b = fibonacci((n//2)-1)

        result = a * ( a+( 2*b ) )

    mat[n] = result%INF
    return result%INF

print(fibonacci(N))
