# 브론즈4
# 인공지능 시계
h, m, s = map(int, input().split())
active_s = int(input())
active_m = (active_s+s)//60
active_h = (active_m+m)//60
active_d = (active_h+h)//24

print((active_h+h)%24, (active_m+m)%60, (active_s+s)%60)

"""
14 30 0
200

17 40 45
6015

23 48 59
2515
"""