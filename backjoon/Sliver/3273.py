# 실버3
# 두 수의 함
import sys
N = int(sys.stdin.readline().strip())
N_list = sorted(list(map(int, sys.stdin.readline().split())))
standard_sum = int(sys.stdin.readline().strip())
result = 0
dic = {}

# 투 포인터
for i in N_list:
    if dic.get(i):
        result += 1
    else:
        dic[standard_sum-i] = 1

print(result)