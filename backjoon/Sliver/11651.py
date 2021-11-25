# 실버5
# 좌표 정렬하기 2
import sys
N = int(sys.stdin.readline())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
T.sort(key=lambda p : (p[1], p[0]))
for i in T: sys.stdout.write(str(i[0])+" "+str(i[1])+"\n")

"""
5
0 4
1 2
1 -1
2 2
3 3

5
0 4
1 -2
1 -1
2 -1
3 3
"""