# 실버3
# 조합
N, M = map(int, input().split())
DP = [0 for _ in range(101)]

def factorial(n):
    if n == 1:
        return n
    else:
        if DP[n] == 0: DP[n] = n*factorial(n-1)
        return DP[n]

# n!/(n-r)!r!
result = factorial(N)//(factorial(N-M)*factorial(M))
print(result)

