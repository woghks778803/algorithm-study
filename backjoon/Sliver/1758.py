# 실버4
# 알바생 강호
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    T = [int(input()) for _ in range(N)]
    T.sort(reverse=True)

    result = 0
    for rank in range(N):
        if T[rank] - rank < 0: break
        else: result += T[rank] - rank
        
    print(result)

"""
4
3
3
3
3

3
3
2
3

5
7
8
6
9
10

5
1
1
1
1
2

3
1
2
3
"""