# 실버1
# 정수 삼각형
import sys
T = int(sys.stdin.readline())

input_list = []
memo_list = []
for i in range(T):
    temp_list = list(map(int, sys.stdin.readline().split()))
    input_list.append(temp_list)
    memo_list.append([0 for j in temp_list])

def dp(h):
    if h == 0:
        memo_list[0][0] = input_list[0][0]
    else:
        end_w = len(memo_list[h])-1
        for w in range(len(memo_list[h])):
            if w == 0:
                memo_list[h][w] = memo_list[h-1][w]+input_list[h][w]
            elif w == end_w:
                memo_list[h][w] = memo_list[h-1][w-1]+input_list[h][w]
            else:
                memo_list[h][w] = max(memo_list[h-1][w], memo_list[h-1][w-1])+input_list[h][w]

h = 0
while True:
    dp(h)
    h += 1
    if h >= T: break
print(max(memo_list[T-1]))



"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
