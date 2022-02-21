# 실버5
# 정열적인 정렬
import sys
output = sys.stdout.write
N = int(input())
T = [int(i) for i in input().split()]
T.sort()
for i in T: output(str(i)+" ")