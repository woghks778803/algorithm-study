# 실버5
# 이장님 초대
N = int(input())
T = [int(i) for i in input().split()]
T.sort()

time = 1
result = 0
while T:
    time += 1
    num = T.pop()
    if time+num > result: result = time+num

print(result)
"""
4
2 3 4 3
"""