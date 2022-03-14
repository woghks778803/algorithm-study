# 실버4
# 피사노 주기
# X
P = int(input())
for _ in range(P):
    N, M = map(int, input().split())
    # m으로 나눴을때 순서 1, 2번째 항값 저장
    # m은 2이상이기때문에 해당 순서는 항상 유지된다
    m1 = m2 = 1
    c = 0

    while True:
        temp = m1
        m1 = m2
        m2 = (temp+m2) % M # m으로 나눈 나머지 저장
        c+=1

        # m으로 나눈 나머지가 초기 1항 2항과 같은 패턴으로 반복되는 구간을 발견시 탈출
        if m1 == 1 and m2 == 1: break 

    print(N, c)

"""
5
1 4
2 5
3 11
4 123456
5 987654
"""