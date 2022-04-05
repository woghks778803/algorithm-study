# 실버3
# 피자 (Large)
def f(n):
    div_n = n//2
    if div_n == 0: return div_n

    if n%2 == 0:
        if not DP.get(div_n):
            DP[div_n] = f(div_n)

        DP[n] = DP[div_n]+DP[div_n]+(div_n**2)
        
    else:
        if not DP.get(div_n+1):
            DP[div_n+1] = f(div_n+1)
        
        if not DP.get(div_n):
            DP[div_n] = f(div_n)

        DP[n] = DP[div_n]+DP[div_n+1]+((div_n+1)*div_n)

    return DP[n]

if __name__ == "__main__":
    n = int(input())
    DP = {}
    print(f(n))
print(DP)

