# 실버4
# 수 찾기
N = int(input())
T1 = sorted(list(map(int, input().split())))
M = int(input())
T2 = list(map(int, input().split()))

result = []
for i in T2:
    min_num = 0
    max_num = N-1
    mid_num = N//2
    check = False
    if i < T1[min_num] or i > T1[max_num] : pass
    else:
        while min_num <= max_num:
            if i > T1[mid_num]:
                min_num = mid_num+1
                mid_num = (max_num + min_num) // 2
            elif i < T1[mid_num]:
                max_num = mid_num-1
                mid_num = (max_num + min_num) // 2
            else:
                check = True
                break
                    
    if check: print(1)
    else: print(0)

"""
5
4 1 5 2 3
5
1 3 7 9 5

5
4 1 6 2 3
5
1 3 7 9 5
"""