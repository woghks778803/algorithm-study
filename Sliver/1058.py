# 실버2
# 친구
import sys
import re
friend_cnt = int(input())
friend_relationship_list = []

for i in range(friend_cnt):
    friend_relationship_list.append(sys.stdin.readline().strip())

directly_friend_list = []
# 일단 직접친구부터 구해보자
for i in friend_relationship_list:
    temp_friend_list = []
    for i in re.finditer("Y", i):
        temp_friend_list.append(i.span()[0])
    directly_friend_list.append(temp_friend_list)
    del temp_friend_list

indirect_friend_list = []
# 간접친구 구하기
# 본인의 친구 중 본인을 제외한 친구들은 모두 자신의 친구이다..
for i in range(len(directly_friend_list)):
    temp_list = []
    # 자신의 친구 목록불러오기
    for j in directly_friend_list[i]:
        # 친구의 친구목록에서 자신을 제외한 친구목록 저장 = 나의 친구의 친구들
        for k in directly_friend_list[j]:
            if i != k:
                temp_list.append(k)
    indirect_friend_list.append(temp_list)
    del temp_list

inssa_user = 0
for i in range(len(directly_friend_list)):
    friend_count = len(set(directly_friend_list[i]+indirect_friend_list[i]))
    if friend_count > inssa_user:
        inssa_user = friend_count
del directly_friend_list
del indirect_friend_list
print(inssa_user)

"""
반례

10
NNNNYNNNNN 
NNNNYNYYNN 
NNNYYYNNNN 
NNYNNNNNNN 
YYYNNNNNNY 
NNYNNNNNYN 
NYNNNNNYNN 
NYNNNNYNNN 
NNNNNYNNNN 
NNNNYNNNNN 
E 
E G H
D E F
C
A B C J
C I
B H
B G
F
E

5
NYNNN
YNYNN
NYNYN 
NNYNY 
NNNYN 
B
A C
B D
C E
D

"""