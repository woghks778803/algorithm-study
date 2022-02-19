# 실버1
# 통나무 건너뛰기
if __name__ == "__main__":
    from collections import deque
    import sys
    input = sys.stdin.readline
    
    for _ in range(int(input())):
        N = int(input())
        T = [int(i) for i in input().split()]
        T.sort()

        dq = deque([])
        cnt = 0
        while T:
            if cnt % 2 == 0: dq.append(T.pop())
            else: dq.appendleft(T.pop())
            cnt += 1

        result = 0
        for i in range(N): 
            diff = abs(dq[i-1] - dq[i])
            if result < diff: result = diff
        print(result)
    
"""
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6
"""