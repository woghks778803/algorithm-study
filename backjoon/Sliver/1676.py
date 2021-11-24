# 실버4
# 팩토리얼 0의 개수
N = int(input())

def count_number(i, j):
    count = 0
    while i:
        i //= j
        count += i
    return count

def factorial(n):
    for i in range(1, n):
        n *= i
    return n    

print(min(count_number(N, 2), count_number(N, 5)))
# count_number(N, 2)
# count_number(N, 5)
# print(count_number(N, 2), count_number(N, 5))
# print(factorial(N))
