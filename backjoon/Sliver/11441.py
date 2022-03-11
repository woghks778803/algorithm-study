# 실버3
# 합 구하기
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    output = sys.stdout.write
    N = int(input())
    A = [int(i) for i in input().split()]
    M = int(input())

    SUM = [0]
    for i in range(N):
        SUM.append(SUM[i]+A[i])
    
    for _ in range(M):
        start, end = map(int, input().split())
        output(str(SUM[end] - SUM[start-1])+"\n")

"""
5
10 20 30 40 50
5
1 3
2 4
3 5
1 5
4 4

3
1 0 -1
6
1 1
2 2
3 3
1 2
2 3
1 3
"""