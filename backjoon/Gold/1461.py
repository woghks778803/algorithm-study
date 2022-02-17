# 골드5
# 도서관
def solve(minus, plus):
    arr = []
    while minus:
        for i in range(M):
            if i == 0: arr.append(abs(minus.pop()))
            elif minus: minus.pop()
            else: break

    while plus:
        for i in range(M):
            if i == 0: arr.append(abs(plus.pop()))
            elif plus: plus.pop()
            else: break

    arr.sort()
    return sum(arr[:-1])*2+arr[-1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    T = [int(i) for i in input().split()]

    plus = []
    minus = []
    for i in T:
        if i > 0: plus.append(i)
        else: minus.append(i)
    plus.sort()
    minus.sort(reverse=True)

    print(solve(minus, plus))








"""
7 2
-37 2 -6 -39 -29 11 -28
39 29 6 11
"""