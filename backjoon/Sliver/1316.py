# 실버5
# 그룹 단어 체커
import sys
N = int(input())
group_list = [list(sys.stdin.readline().strip()) for i in range(N)]

group_cnt = 0
for group in group_list:
    temp_dic = {}
    chk_group = True
    previous_char = None
    for i in group:
        if previous_char == None or temp_dic.get(i) == None: # 이전값이 없음 or 해당값이 처음이면 저장
            temp_dic[i] = True
            previous_char = i
        elif previous_char == i: # 이전순번과 같은값이면 패스
            pass
        else:
            chk_group = False
            break
    if chk_group:
        group_cnt += 1

print(group_cnt)