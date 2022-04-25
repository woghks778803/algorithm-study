# 실버2
# 주식
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    prices = [int(i) for i in input().split()]
    max_num = prices.pop()
    result = 0

    while prices:
        check_num = prices.pop()
        if check_num > max_num:
            max_num = check_num
        else:
            result += max_num - check_num        

    print(result)


"""
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
"""