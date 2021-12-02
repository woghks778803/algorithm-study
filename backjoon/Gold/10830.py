# 골드4
# 행렬 제곱
import sys
INF = 1000
N, B = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

def my_pow(arr ,b):
    if b == 1: return arr
    
    p = my_pow(arr, b//2)
    multi = mat_multi(p, p)

    if b%2 == 1: return mat_multi(arr, multi)
    else: return multi

def mat_multi(A, B):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N): C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= INF
    return C

result = my_pow(T, B)

for row in result:
    for col in row: 
        col = col%INF
        sys.stdout.write(str(col)+" ")
    sys.stdout.write("\n")
# print(result)
# print(i,k, k,j)
"""
2 5
1 2
3 4

3 3
1 2 3
4 5 6
7 8 9

5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1

5 100000000000
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1

2 1
1000 1000
1000 1000
"""