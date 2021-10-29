# 실버3
# GCD 합
test_case_cnt = int(input())
test_case_list = []

for i in range(0, test_case_cnt):
    test_case_list.append(list(map(int, input().split())))

for test_case in test_case_list:
    sum_yaksu = 0
    # 케이스별 최대공약수 도출
    for i in range(1, test_case[0]+1):
        for j in range(i+1, test_case[0]+1):
            # 동일케이스 비교시 종료
            if test_case[0]+1 == j:
                break
            
            max_yaksu = 1
            # 최대공약수 알고리즘
            if test_case[i] >= test_case[j]:
                for k in reversed(range(2, test_case[j]+1)):
                    if test_case[i] % k == 0 and test_case[j] % k == 0:
                        max_yaksu = k
                        break
            elif test_case[i] < test_case[j]:
                for k in reversed(range(2, test_case[i]+1)):
                    if test_case[i] % k == 0 and test_case[j] % k == 0:
                        max_yaksu = k
                        break
            sum_yaksu += max_yaksu
    print(sum_yaksu)



# for k in reversed(range(2, 10+1)):
#     print(k)
# test_num_list = []
# # 대조값 정렬
# for i in range(1, test_case[0]+1):
#     test_num_list.append(test_case[i])
# test_num_list.sort()
# 1 3
# 1 7
# 1 5
# 1 2 3 4 6 12

# 10 20 = 10
# 10 30 = 10
# 10 40 = 10
# 20 30 = 10
# 20 40 = 20
# 30 40 = 10

# 7 5 = 1
# 7 12 = 1
# 5 12 = 1

# 15 25 = 5
# 125 15 = 5
# 125 25 = 25