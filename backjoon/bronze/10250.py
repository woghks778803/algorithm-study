# 브론즈3
# ACM 호텔
N = int(input())

for i in range(N):
    h, w, n = map(int, input().split())

    h_r = n % h
    w_r = (n // h)

    if h_r == 0: h_r = h
    else: w_r += 1

    if w_r < 10: w_r = '0'+str(w_r)

    print(str(h_r)+str(w_r))

"""
2
6 12 10
30 50 72

5
12 12 12
12 12 144
12 12 1
12 12 11
12 12 24
"""