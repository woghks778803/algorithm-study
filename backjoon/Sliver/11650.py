# 실버5
# 좌표 정렬하기
import sys
N = int(sys.stdin.readline())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
T.sort(key=lambda p : (p[0], p[1]))
for i in T: sys.stdout.write(str(i[0])+" "+str(i[1])+"\n")

"""
5
3 4
1 1
1 -1
2 2
3 3
"""