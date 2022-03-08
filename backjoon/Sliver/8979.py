# 실버5
# 올림픽 
N, K = map(int, input().split())
T = [[int(i) for i in input().split()] for _ in range(N)]
T.sort(key= lambda x : (-x[1], -x[2], -x[3]))

rank = 1
rank_list = { T[0][0] : rank }
stack = 0
for i in range(1, N):
    if T[i-1][1] == T[i][1] and T[i-1][2] == T[i][2] and T[i-1][3] == T[i][3]:
        stack += 1
        rank_list[T[i][0]] = rank
    else:
        rank += 1
        rank += stack
        rank_list[T[i][0]] = rank
        stack = 0

print(rank_list[K])
print(rank_list)

"""
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1

5 5
1 5 0 0
2 4 0 0
3 3 0 0
4 4 0 0
5 1 0 0
"""