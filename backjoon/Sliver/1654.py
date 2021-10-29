# 실버3
# 랜선 자르기
import sys
K, N = list(map(int, input().split()))
lan_list = []
for i in range(K):
    lan_list.append(int(sys.stdin.readline()))

min_num = max(lan_list)//N
max_num = sum(lan_list)
standard = (min_num+max_num)//2

# 이분탐색 알고리즘
def check_count(standard, max_num, min_num):
    max_standard = max_num
    min_standard = min_num
    while True:
        # 기준값으로 랜선 수 구하기
        lan_count = 0
        for i in range(len(lan_list)): lan_count += lan_list[i]//standard

        # 랜선 수 비교
        if N > lan_count:
            max_standard = standard
            standard = (standard+min_standard)//2
        else:
            min_standard = standard
            if standard == (min_standard+max_standard)//2: break
            else: standard = (standard+max_standard)//2
            
    return standard
# 최초 기준선
result = check_count(standard, max_num, min_num)
print(result)

# print(min_standard, max_standard, standard, lan_count)
"""
반례
4 11
802
743
457
539

4 5
10
1
1
1

4 11
900 
543 
457 
539 

4 4
100
100
100
100

3 5
5
5
4
"""