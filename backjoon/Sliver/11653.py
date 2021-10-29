# 실버
# 소인수분해
N = int(input())

def recursion(N):
    for i in range(2, N+1):
        if N%i == 0:
            print(i)
            recursion(N//i)
            break
        
if N == 1:
    pass
else:
    recursion(N)

"""

72
36
18

"""