# 실버2
# 동전 0
money_cnt, money_cost = map(int, input().split())

money_input_list = []
money_min_list = []

# 입력값 리스트 저장
for i in range(money_cnt):
    money_input_list.append(int(input()))

# 입력값 내림차순 정렬
for money_input in money_input_list:
    if money_cost > money_input :
        money_min_list.append(money_input)
money_min_list.sort(reverse=True)

# 최솟값 경우의 수 알고리즘
count = 0
while True:
    if money_cost == money_min_list[0]:
        count += 1
        break
    elif money_cost == 0:
        break
    elif money_cost % money_min_list[0] == 0:
        count += int(money_cost/money_min_list[0])
        break
    else:
        count += int(money_cost/money_min_list[0])
        money_cost = money_cost % money_min_list[0]
        del money_min_list[0]
    
print(count)

# 반례
# 6 2430
# 1 
# 300 
# 1800 
# 7200 
# 14400
# 28800

# 6 360
# 1
# 15
# 60
# 300
# 1500
# 4500

# 10 4200
# 1
# 10
# 5
# 100
# 500
# 50
# 1000
# 5000
# 10000
# 50000