# 실버5
# 수 정렬하기 3
import sys
N = int(sys.stdin.readline())
INF = 10001
T = [0 for _ in range(INF)]
for i in range(N): T[int(sys.stdin.readline())] += 1

for i in range(INF):
    for j in range(T[i]):
        sys.stdout.write(str(i)+"\n")


"""
10
5
2
3
1
4
2
3
5
1
7
"""