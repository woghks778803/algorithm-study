# 실버2
# 연속합
# X
N = int(input())
test_case = list(map(int, input().split()))

sum = 0
sum_list = []
if max(test_case) < 0:
    print(max(test_case))
else:
    for i in range(len(test_case)):
        if test_case[i]+sum < 0:
            sum = 0
            continue
        sum += test_case[i]
        sum_list.append(sum)
    print(max(sum_list))

