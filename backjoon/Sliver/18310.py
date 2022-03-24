# 실버3
# 안테나
import sys
n = int(sys.stdin.readline().rstrip()) #4
n_list = list(map(int,sys.stdin.readline().split())) # 5 1 7 9
n_list.sort()

print(n_list[(n-1)//2])
"""
4
5 1 7 9
"""