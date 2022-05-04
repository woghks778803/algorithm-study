# 브론즈1
# 일곱 난쟁이
def dfs(index, sum_num, arr):
    for i in range(index, 9):
        temp_arr = arr.copy()
        temp_arr.append(T[i])

        global complete
        if len(temp_arr) < 7 and not complete:
            dfs(i+1, sum_num+T[i], temp_arr)
        elif sum_num+T[i] == 100:
            complete = True
            temp_arr.sort()
            for t in temp_arr: print(t)

T = [int(input()) for _ in range(9)]
complete = False
dfs(0, 0, [])

"""
20
7
23
19
10
15
25
8
13
"""