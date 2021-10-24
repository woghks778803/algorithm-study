# 실버4
# 통계학
import sys
from collections import Counter
test_case=[]
test_case_cnt=int(input())
for i in range(test_case_cnt):
    test_case.append(int(sys.stdin.readline()))
test_case.sort()

d=Counter(test_case)
M=max(d.values())
m=0
for i in range(test_case_cnt):
    if (i==0)|(test_case[i-1]!=test_case[i]):k=1
    else:k+=1
    if M==k:
        if m:m=test_case[i];break
        else:m=test_case[i]

print('%.0f'%(sum(test_case)/test_case_cnt),test_case[(test_case_cnt-1)//2],m,max(test_case)-min(test_case),sep='\n')