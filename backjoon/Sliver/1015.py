# 실버4
# 수열 정렬
N = int(input())
A = input().split()

T = [(int(A[i]), i) for i in range(N)]
T.sort()

dic = {}
for i in range(N): dic[T[i][1]] = i

for i in range(N):
    print(dic[i], end=" ")

"""
3
2 3 1

4
2 1 3 1
"""