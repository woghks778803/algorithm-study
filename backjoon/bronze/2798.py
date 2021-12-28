# 브론즈2
# 블랙잭 
def blackjack(index, sum_num, count):
    for i in range(index+1, N):
        if count+1 == 3:
            global ans
            if M >= sum_num+T[i] and ans < sum_num+T[i]:
                ans = sum_num+T[i]
        else:
            blackjack(i, sum_num+T[i], count+1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    T = list(map(int, input().split()))
    ans = 0
    for index in range(N): blackjack(index, T[index], 1)
    print(ans)


"""
5 21
5 6 7 8 9

10 500
93 181 245 214 315 36 185 138 216 295

5 213
213 12 23 2 1

5 213
12 213 23 2 1

5 213
12 1 2 1 213
"""