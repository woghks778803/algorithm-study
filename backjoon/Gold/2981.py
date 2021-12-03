# 골드5
# 검문
N = int(input())
T = [int(input()) for _ in range(N)]
# 공식 - 유클리드 호제법
def uc(b, s):
    while True:
        if b % s == 0: break
        temp = b
        b = s
        s = temp % s
    return s

b = abs(T[1] - T[0])
for i in range(1, N):
    a = T[i]
    b = uc(abs(T[i] - T[i-1]), b)

divisorsList = []

for i in range(2, int(b**(1/2)) + 1):
    if (b % i == 0):
        divisorsList.append(i) 
        if ( (i**2) != b) : 
            divisorsList.append(b // i)

divisorsList.sort()

if not divisorsList: print(b)
else: print(str(divisorsList).replace("[","").replace("]","").replace(",",""), b)

"""
2
99999990
999999891

3
6
34
38

5
5
17
23
14
83

3
15
35
75

2
7
17

3
999999999 
234234234 
345345345

3 
9 
333667 
1001001 
3003003
"""