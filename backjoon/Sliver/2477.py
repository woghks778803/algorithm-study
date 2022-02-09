# 실버4
# 참외밭
from collections import defaultdict, Counter
N = int(input())
lst = []
graph = defaultdict(list)

for _ in range(6):
    a, b = map(int, input().split())
    graph[a].append(b)
    lst.append(a)
counter = Counter(lst)

cnt_lst = [] # 등장하는 값의 순서대로 카운터 저장 
cnt2_lst = [] # 카운터 갯수가 2개인 값 등장 순서
for i in lst[:4]: 
    cnt_lst.append(counter[i])
    if counter[i] == 2: cnt2_lst.append(i)

big_square = 1 # 큰 사각형 넓이
for i in counter:
    if counter[i] == 1: big_square *= graph[i][0]

# 작은 사각형 넓이
if cnt_lst == [2,2,2,1]: small_square = (graph[cnt2_lst[0]][0]*graph[cnt2_lst[1]][0])
elif cnt_lst == [2,2,1,1]: small_square = (graph[cnt2_lst[0]][0]*graph[cnt2_lst[1]][1])
elif cnt_lst == [2,1,1,2]: small_square = (graph[cnt2_lst[0]][1]*graph[cnt2_lst[1]][1])
else: small_square = (graph[cnt2_lst[0]][1]*graph[cnt2_lst[1]][0])

print((big_square- small_square)*N)
# print(big_square, small_square)
# print(lst, graph, counter)

"""
7
4 50
2 160
3 30
1 60
3 20
1 100

5
3 20
1 50
4 60
2 30
3 40
2 20

5
3 40
2 20
3 20
1 50
4 60
2 30
"""