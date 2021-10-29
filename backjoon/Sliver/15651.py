# 실버3
# N과 M (3)
import sys
N, M = map(int, sys.stdin.readline().split())

def recursion(index, str_num):
    index += 1
    for num in range(1, N+1):
        temp_num = str_num
        temp_num += str(num)+" "

        if index < M:
            recursion(index, temp_num)
        else:
            print(temp_num)


for num in range(1, N+1):
    index = 1
    str_num = str(num)+" "
    if index < M:
        recursion(index, str_num)
    else:
        print(str_num)


