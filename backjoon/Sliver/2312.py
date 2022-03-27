# 실버3
# 수 복원하기
def find_sosu():
    num = [False for _ in range(100001)]

    for i in range(2, 100001):
        if num[i]: continue
        sosu.append(i)

        for j in range(i, 100001, i):
            num[j] = True

    del num

def solve():
    T = int(input())
    for i in range(T):
        N = int(input())
        result = {}

        for s in sosu:
            while True:
                if N%s == 0:
                    N //= s
                    if result.get(s): result[s] += 1
                    else: result[s] = 1
                else:
                    break
        
        for r in result.items():
            print(*r)   
            
if __name__ == "__main__":
    sosu = []
    find_sosu()
    solve()


"""
2
6
24
"""