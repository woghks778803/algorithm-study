# 실버3
# 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

def solve():
    cnt = 0
    a_point = 0
    b_point = 0

    while b_point < M:

        if A[a_point] > B[b_point]: # a가 b보다 큰 경우 쌍값 카운터
            cnt += 1
            b_point += 1
        else:
            a_point += 1

            # a 위치가 크기를 초과할 경우 종료
            # 그렇지않을경우 현재까지 도달한 b의 갯수는 다음 a보다 작기때문에 카운터 처리
            if a_point < N: cnt += b_point
            else: break
    
    # 미처리된 a보다 작은 b의 쌍값 처리
    if a_point < N:
        cnt += b_point*(N-(a_point+1))

    return cnt

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        A = [int(i) for i in input().split()]
        B = [int(i) for i in input().split()]

        A.sort()
        B.sort()

        result = solve()
        print(result)

"""
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215


1
5 3
8 1 7 3 1
3 6 1
"""