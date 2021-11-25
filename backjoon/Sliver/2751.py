# 실버5
# 수 정렬하기 2
import sys
N = int(sys.stdin.readline())
T = [int(sys.stdin.readline()) for _ in range(N)]
T.sort()
for i in T: sys.stdout.write(str(i)+"\n")
"""
5
5
4
3
2
1

5
5
4
-3
-2
1
"""