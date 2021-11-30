# 골드1
# 이항 계수 3
# X
N, K = map(int, input().split())
INF = 1000000007

# 페르마의 소정리
def my_pow(a, b):
    ans = 1
    while b > 0:
        print(b)
        print(ans)
        if b % 2 == 1:
            ans = (ans*a) % INF
        a = (a*a) % INF
        b //= 2
    return ans
    # if b == 1:
    #     return a%INF
    # else:
    #     p = my_pow(a, b//2)
    #     if b%2 == 1:
    #         return p*p*a%INF
    #     else:
    #         return p*a%INF

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = (result*i)%INF
    return result

if N == K or K == 0:
    print(1)
else:
    print((factorial(N) * my_pow(factorial(N-K)*factorial(K), INF-2)) % INF)
    # print(factorial(N)//(factorial(N-K)*factorial(K)))
