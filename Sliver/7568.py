# 실버5
# 덩치
import sys
user_cnt = int(input())
user_list = []

for i in range(user_cnt):
    user_list.append(list(map(int, sys.stdin.readline().split())))

for i in user_list:
    rank = 1
    for j in user_list:
        if j[0] > i[0] and j[1] > i[1]:
            rank += 1
    i.append(rank)

for i in user_list:
    print(i[2],end=" ")
