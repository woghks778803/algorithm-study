# 실버3
# 수강신청
import sys
input = sys.stdin.readline
output = sys.stdout.write
N, M = map(int, input().split())
T = {}

for i in range(M):
    input_num = input().strip()
    T[input_num]=i

lst = list(T.items())
lst.sort(key= lambda x : (x[1]))
len_lst = len(lst)

for i in range(N): 
    if len_lst > i: output(lst[i][0]+'\n')
    else: break
"""
3 8
20103324
20133221
20133221
20093778
20140101
01234567
20093778
20103325
"""