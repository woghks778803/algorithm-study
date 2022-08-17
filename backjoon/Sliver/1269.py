# 실버4
# 대칭 차집합
def intersection(d1, d2, result):
    cnt = 0

    for i in d1:
        if d2.get(i): cnt += 1
    
    print(result-(cnt*2))

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())

    A = {i:True for i in input().split()}
    B = {i:True for i in input().split()}

    if N<M:
        intersection(A,B,N+M)
    else:
        intersection(B,A,N+M)

'''
3 5
1 2 4
2 3 4 5 6
'''