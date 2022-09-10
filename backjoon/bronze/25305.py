# 브론즈2
# 커트라인
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
points = [int(i) for i in input().split()]

points.sort(reverse=True)

print(points[K-1])

"""
5 2
100 76 85 93 98
"""