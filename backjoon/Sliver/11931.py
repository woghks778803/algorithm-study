# 수 정렬하기 4
# 실버5
import sys
input = sys.stdin.readline
output = sys.stdout.write
T = [int(input()) for _ in range(int(input()))]
T.sort(reverse=True)
for t in T: output(str(t)+"\n")

"""
5
1
2
3
4
5
"""