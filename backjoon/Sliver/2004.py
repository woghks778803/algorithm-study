# 실버2
# 조합 0의 개수
N, M = map(int, input().split())

def count_number(i, j):
    count = 0
    while i:
        i //= j
        count += i
    return count

print(min(count_number(N,2) - count_number(N-M,2) - count_number(M,2), count_number(N,5) - count_number(N-M,5) - count_number(M,5)))
# print(min(count_number(N,2), count_number(N,5)) - min(count_number(N-M,2), count_number(N-M,5)) - min(count_number(M,2), count_number(M,5)))
# print(count_number(N,2), count_number(N-M,2), count_number(M,2), count_number(N,5), count_number(N-M,5), count_number(M,5))

"""
25 12
"""