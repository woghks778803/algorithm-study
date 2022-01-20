# 실버5
# 온라인 판매
N, M = map(int, input().split())
T = [int(input()) for _ in range(M)]
T.sort(reverse=True)
result = []

for i in range(M):
    if i+1 <= N: result.append(T[i]*(i+1))
    else: result.append(T[i]*N)
        
max_result = max(result)
for i in  reversed(range(M)):
    if result[i] == max_result:
        print(T[i], max_result)
        break

# print(T)
# print(result)

"""
5 4
2
8
10
7

10 4
17
16
11
15

3 4
12
9
6
3

"""