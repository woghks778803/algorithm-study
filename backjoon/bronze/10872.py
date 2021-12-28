# 브론즈3
# 팩토리얼
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    N = int(input())
    print(factorial(N))
