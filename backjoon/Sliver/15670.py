# 실버3
# N과 M (2)
import sys
from itertools import combinations 
N, M = map(int, sys.stdin.readline().split())

n_list = [i for i in range(1, N+1)]
result_list = combinations(n_list, M)
for result_ele in result_list:
    result_str = ""
    for i in range(len(result_ele)):
        result_str += str(result_ele[i]) + " "
    print(result_str)
