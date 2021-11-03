# 실버5
# 체스판 다시 칠하기
import sys
N, M = map(int, sys.stdin.readline().split())

chess_list = []
for i in range(N):
    chess_list.append(list(sys.stdin.readline().strip()))

# 시작값 구분하기
def reverse_type(check_type):
    if check_type == "W":
        check_type = "B"
    else:
        check_type = "W"
    return check_type

# 8*8 범위 내의 변화값 구하기
def find_chess(check_type, change_count, start_x, start_y):
    for y in range(start_y, start_y+8):
        check_type = reverse_type(check_type)

        for x in range(start_x, start_x+8):
            if check_type != chess_list[y][x]:
                change_count += 1

            check_type = reverse_type(check_type)
    return change_count

start_type = ["W", "B"]
change_list = []
for y in range(len(chess_list)-7):
    for x in range(len(chess_list[y])-7):

        for i in start_type:
            change_count = 0
            check_type = i
            # 시작값, 변화횟수, 시작 범위 좌표(x, y)
            change_count = find_chess(check_type, change_count, x, y)
            change_list.append(change_count)
# 최소 변화값
print(min(change_list))
"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

8 8
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB

9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW

10 10
BBBBBBBBBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB

8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWWWB
BWBWBWBW

11 12
BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
"""