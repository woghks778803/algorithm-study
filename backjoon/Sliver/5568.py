# 실버4
# 카드 놓기
import itertools
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
T = [int(input()) for _ in range(N)]

result = 0
dct = {}
arr = itertools.permutations(T, K)
for i in arr:
    temp = ""
    
    for j in i: temp += str(j)

    if not dct.get(temp): 
        dct[temp] = True
        result += 1

print(result)


"""
4
2
1
2
12
1
"""