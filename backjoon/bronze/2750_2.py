# 브론즈1
# 수 정렬하기
N = int(input())
T = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if T[i] < T[j]:
            temp = T[i]
            T[i] = T[j]
            T[j] = temp

for i in T: print(i)

"""
5
5
2
3
4
1
"""