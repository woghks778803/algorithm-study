# 실버3
# ATM
user_cnt = int(input())
time_list = list(map(int,input().split()))
time_list.sort()

result_min_time = 0
sum_time = 0
for i in time_list:
    sum_time += i
    result_min_time += sum_time 
print(result_min_time)