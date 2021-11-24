# 실버1
# 이항 계수2
N, K = map(int, input().split())
INF = 10007

def factorial(n):
    if n == 0: return 1 
    for i in range(1, n):
        n *= i 
    return n

print( factorial(N)//(factorial(N-K)*factorial(K)) % INF )