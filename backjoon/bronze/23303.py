# 브론즈2
# 이 문제는 D2 입니다.
import re
st = input()
comp = re.compile("(D2|d2)")
ans = re.search(comp, st)

if ans == None: print("unrated")
else: print("D2")