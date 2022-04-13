# 실버4
# 세 개의 소수 문제
def printSum(num):
    cnt = 0
    for p in prime:
        if p < num: cnt += 1
        else: break
    
    for p1 in prime[:cnt]:
        for p2 in prime[:cnt]:
            for p3 in prime[:cnt]:
                if p1+p2+p3 == num:
                    print(p1, p2, p3)
                    return
    
    print(0)

# 에라토스테네스의 체
def findPrime():
    DP = [False for _ in range(1001)]
    prime = []
    for i in range(2, 1001):
        if DP[i]: continue
        prime.append(i)

        for j in range(i, 1001, i): DP[j] = True
    del DP

    return prime

if __name__ == "__main__":
    T = int(input())
    prime = findPrime()

    for i in range(T):
        num = int(input())
        printSum(num)


"""
3
7
11
25

3
15
7
100
"""