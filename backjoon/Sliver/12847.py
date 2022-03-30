# 실버3
# 꿀 아르바이트
N, M = map(int , input().split())
T = [int(i) for i in input().split()]

sum_num = sum(T[:M])
result = sum_num

for i in range(1, N-M+1):
    sum_num = sum_num-T[i-1]+T[i+M-1]
    if sum_num > result: result = sum_num

print(result)

"""
5 3
10 20 30 20 10

25000
"""