# 실버4
# 제로
import sys
N = int(sys.stdin.readline())

result_list = []
for i in range(N):
    T = int(sys.stdin.readline())
    if T == 0 and not result_list: pass
    elif T == 0: result_list.pop()
    else: result_list.append(T)

if not result_list: print(0)
else: print(sum(result_list))