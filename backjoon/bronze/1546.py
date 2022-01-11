# 브론즈1
# 평균
N = int(input())
T = list(map(int, input().split()))
max_num = max(T)

update_score = [i for i in map(lambda x : x/max_num*100, T)]
print(sum(update_score)/len(update_score))

"""
3
40 80 60

3
10 20 30

4
1 100 100 100

5
1 2 4 8 16

2
3 10
"""