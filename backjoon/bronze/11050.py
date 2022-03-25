# 브론즈1
# 이항 계수 1
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        if DP[n-1] == 0:
            DP[n-1] = factorial(n-1)
        return n * DP[n-1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    DP = [0 for _ in range(11)]

    print(factorial(N) // (factorial(N-M) * factorial(M)))
    # print(factorial(N))
    # print(factorial(N-M))
    # print(factorial(M))


