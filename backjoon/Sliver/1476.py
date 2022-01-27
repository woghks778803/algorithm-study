# 실버5
# 날짜 계산
E, S, M = map(int, input().split())
if E == 15: E = 0
if S == 28: S = 0
if M == 19: M = 0

for i in range(1, (15*28*19)+1): 
    if i%15 == E and i%28 == S and i%19 == M: 
        print(i)
        break


"""
2 2 2
1 16 16 = 16
2 17 17 = 17
13 28 9 = 28
15 28 19 = 7980
"""