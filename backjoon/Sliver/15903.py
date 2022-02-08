# 실버2
# 카드 합체 놀이
if __name__ == "__main__":
    N, M = map(int, input().split())
    T = [int(i) for i in input().split()]
    T.sort()
    cnt = 0

    while cnt != M:
        cnt += 1
        T[0] = T[1] = T[0] + T[1]
        T.sort()
    print(sum(T))
    
"""
3 1
3 2 6

4 2
4 2 3 1
"""