# 실버3
# N과 M (4)
import copy
N, M = map(int, input().split())

num_list = [i for i in range(1, N+1)]
result_list = []

def recursion(count, previous_index, save_list):
    count += 1
    for i in range(previous_index, len(num_list)):
        temp_list = copy.deepcopy(save_list)
        temp_list.append(num_list[i])

        if count < M:
            recursion(count, i, temp_list)
        else:
            result_list.append(temp_list)

for i in range(len(num_list)):
    count = 1
    if count >= M:
        print(num_list[i])
    else:
        save_list = [num_list[i]]
        recursion(count, i, save_list)

for i in result_list:
    result_message = ""
    for j in i:
        result_message += str(j) + " "
    print(result_message)
    

