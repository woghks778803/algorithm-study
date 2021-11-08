# 실버3
# 01타일
N = int(input())

# 피보나치 규칙으로 구했을때
arr = [0] * (N+1) # N값이 1일때 인덱스 오류방지
arr[0] = 1
arr[1] = 2

# 15746는 임의값 
# 이해 안될경우 mod에 대한 1629번 해설 참조
for i in range(N-2):
    arr[i+2] = (arr[i] + arr[i+1])%15746

print(arr[N-1]%15746)

"""
5
=8
4
=5
3
=3
2
=2
1
=1
"""

# 순수하게 모든 항을 계산할때

# count = 0
# result_list = []
# limit_num = pow(2, N)

# for i in range(limit_num):
#     temp_list = [0 for _ in range(N)]
#     index = 0
#     mok = i
#     while mok != 0:
#         temp_list[index] = mok%2
#         mok = mok//2
#         index += 1
    
#     remove_type = False
#     zero_continue_cnt = 0
#     previous_num = temp_list[0]
#     if temp_list[0] == 0:
#         zero_continue_cnt += 1
#     for j in range(1, len(temp_list)):
#         if temp_list[j] == 0:
#             zero_continue_cnt += 1
#         else:
#             if previous_num == 0 and zero_continue_cnt%2 == 1:
#                 remove_type = True
#                 break
#         previous_num = temp_list[j]

#     if previous_num == 0 and zero_continue_cnt%2 == 1:
#         remove_type = True

#     if not remove_type:
#         result_list.append(temp_list)
        
# print(len(result_list))