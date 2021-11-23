# 골드5
# AC
import sys
import collections
N = int(sys.stdin.readline())

for i in range(N):
    F = list(map(str, sys.stdin.readline().strip()))
    FN = int(sys.stdin.readline())
    arr_str = sys.stdin.readline().strip()
    arr_str = arr_str.replace("[","").replace("]","")
    if arr_str: arr = list(map(int, arr_str.split(",")))
    else: arr = []
    deq = collections.deque(arr)

    error_check = False
    reverse_toggle = False
    reverse_count = F.count("R")
    for i in F:
        if i == "R": 
            if reverse_toggle: reverse_toggle = False
            else: reverse_toggle = True

        elif i == "D":
            if deq: 
                if reverse_toggle: deq.pop()
                else: deq.popleft()
            else:
                error_check = True
                print("error")
                break

    if F.count("R") % 2 == 1: deq.reverse()

    if not error_check: 
        print(str(list(deq)).replace(" ",""))

"""
6
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
RDRDDRD
6
[1,1,2,3,5,8]
D
0
[]
R
0
[]


DRDRDD
6
[1,1,2,3,5,8]
"""