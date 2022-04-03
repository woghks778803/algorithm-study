# 실버2
# 팰린드롬 파티션
DP = [0 for _ in range(1001)]
DP[1] = 1
DP[2] = 2
DP[3] = 2

for i in range(4, 1001):
    num = i
    save = 0
    while num >= 0:
        if num == i: save += 1
        else: save += DP[(i-num)//2]
        num -= 2
    DP[i] = save

T = int(input())
for _ in range(T):
    n = int(input())
    print(DP[n])


"""
3
4 = 1 2 1, 1 1 1 1, 4, 2 2
7
20

"""