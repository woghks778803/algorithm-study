# 브론즈2
# 벌집
if __name__ == "__main__":
    N = int(input())
    INF = 6
    ans = 1
    n = 1

    while N > n:
        n += INF*ans
        ans += 1
        
    print(ans)
