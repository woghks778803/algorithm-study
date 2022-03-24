# 실버5
# 종이자르기
w, h = map(int, input().split())
N = int(input())

# 시작값과 길이 저장
w_lst = [0, h] # 가로 자르기
h_lst = [0, w] # 세로 자르기

for _ in range(N):
    position, point = map(int, input().split())

    if position == 0: w_lst.append(point)
    else: h_lst.append(point)

w_lst.sort()
h_lst.sort()

w_result = []
for i in range(1, len(w_lst)):
    w_result.append(w_lst[i] - w_lst[i-1])

h_result = []
for i in range(1, len(h_lst)):
    h_result.append(h_lst[i] - h_lst[i-1])
print(max(w_result)*max(h_result))
print(w_lst, h_lst)

"""
10 8
3
0 3
1 4
0 2
"""