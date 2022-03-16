# 실버5
# K번째 수
N, K = map(int, input().split())
T = [int(i) for i in input().split()]
T.sort()
print(T[K-1])
print(T)

"""
5 2
4 1 2 3 5
"""