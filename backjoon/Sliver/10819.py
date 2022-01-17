# 실버2
# 차이를 최대로
import copy
from collections import deque

def dfs(lst, num, ans):
    for _ in range(len(lst)):
        pop_num = lst.pop()
        temp_lst = copy.deepcopy(lst)

        global result
        if result < ans+abs(num-pop_num): result = ans+abs(num-pop_num)

        dfs(temp_lst, pop_num, ans+abs(num-pop_num))
        lst.appendleft(pop_num)

if __name__ == "__main__":
    N = int(input())
    lst = deque(map(int, input().split()))
    result = 0

    for i in range(N-1):
        pop_num = lst.pop()
        temp_lst = copy.deepcopy(lst)

        dfs(temp_lst, pop_num, 0)
        lst.appendleft(pop_num)

    print(result)


"""
6
20 1 15 8 4 10
"""