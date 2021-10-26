# 실버4
# 주유소
import sys
N = int(input())

length_list = list(map(int, sys.stdin.readline().split()))
cost_list = list(map(int, sys.stdin.readline().split()))

result = 0
min_cost = 0
for i in range(N-1):
    if i == 0:
        min_cost = cost_list[i]
    min_cost = min(min_cost, cost_list[i])
    result += min_cost*length_list[i]
print(result)