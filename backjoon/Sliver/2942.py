# 실버2
# 퍼거슨과 사과

# 유클리드 호제법
def uc(a, b):
    while True:
        temp = b
        b = a % b
        if b == 0: return temp
        else: a = temp

if __name__ == "__main__":
    R, G = map(int, input().split())

    gcd = uc(R, G)

    # 최대공약수의 약수구하기
    divisorsList = [1, gcd]
    for i in range(2, int(gcd**(1/2)) + 1):
        if (gcd % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != gcd) : 
                divisorsList.append(gcd // i)

    for i in divisorsList: print(i, R//i, G//i)


"""
1000000000 952151251
2 4
42 105
4200000000 8400000000
"""