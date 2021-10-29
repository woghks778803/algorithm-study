# 실버3
# N과 M(1)
import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
N_list = [i for i in range(1, N+1)]

result_permutations = permutations(N_list, M)
for result_list in result_permutations:
    result_str = ""
    for j in result_list:
        result_str += str(j)+" "
    print(result_str)
