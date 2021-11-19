# 실버3
# 스택 수열
import sys
N = int(sys.stdin.readline())
T = [int(sys.stdin.readline()) for _ in range(N)]

fail_check = False
temp_data = []
result = []
index = 0
in_num = 1
while N > index:

    if len(temp_data) > 0 and T[index] == temp_data[-1]:
        temp_data.pop()
        result.append("-")
        index += 1
    else:
        if in_num > N:
            fail_check = True
            break
        temp_data.append(in_num)
        result.append("+")
        in_num += 1

if fail_check: print("NO")
else: 
    for i in result: print(i)

"""

8
4
3
6
8
7
5
2
1

5
1
2
5
3
4

5
3
2
1
4
5
"""