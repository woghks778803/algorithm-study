# 실버3
# 이친수
# DP[i] = sum(DP[1:i-1]) + 1 # ... 걍 피보나치네
if __name__ == "__main__":
    N = int(input())
    DP = [0 for _ in range(91)]
    DP[1] = 1
    DP[2] = 1

    for i in range(3, 91): DP[i] = DP[i-1] + DP[i-2]
    
    print(DP[N])



