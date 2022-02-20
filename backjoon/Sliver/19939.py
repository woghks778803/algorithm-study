# 실버5
# 박 터뜨리기
N, K = map(int, input().split())
sum_num = 0

for i in range(1, K+1):
    sum_num += i
N -= sum_num

if N < 0:
    print(-1)
else:
    if N%K == 0: print(K-1)
    else: print(K)


"""
30 15
15 5
15 3
22 4
11 2
"""