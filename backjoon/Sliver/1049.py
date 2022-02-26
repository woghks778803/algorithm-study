# 실버4
# 기타줄
N, M = map(int, input().split())
result = 0
package = int(1e12)
individual = int(1e12)

for i in range(M):
    a, b = map(int, input().split())
    if a < package: package = a
    if b < individual: individual = b

individual_result = individual*(N%6)
package_result = package*(N//6)
if individual*6 < package: print(individual*N)
elif individual_result < package : print(package_result+individual_result)
else: print(package_result+package)

"""
4 2
12 3
15 4

10 3
20 8
40 7
60 4

15 1
100 40

9 16
21 25
77 23
23 88
95 43
96 19
59 36
80 13
51 24
15 8
25 61
21 22
3 9
68 68
67 100
83 98
96 57
"""