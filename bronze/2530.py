# 브론즈4
# 인공지능 시계
h, m, s = map(int, input().split())
active_s = int(input())

active_m = int((active_s+s)/60)
mod_s = (active_s+s)%60 

active_h = int((active_m+m)/60)
mod_m = (active_m+m)%60 

active_d = int((active_h+h)/24)
mod_h = (active_h+h)%24 

print(mod_h, mod_m, mod_s)