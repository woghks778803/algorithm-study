# 실버3
# 시리얼 번호
import re
N = int(input())
T = [input() for _ in range(N)]

arr = []
for i in range(N):
    sub_string = re.subn("[A-Z]", "", T[i])
    if len(sub_string[0]) < 1:
        arr.append([T[i], len(T[i]), 0])
    else:
        temp_sum = 0
        for j in map(int, list(sub_string[0])):
            temp_sum += j
        arr.append([T[i], len(T[i]), temp_sum])

arr.sort(key= lambda x: (x[1], x[2], x[0]))
for i in arr: print(i[0])

"""
5
ABCD
145C
A
A910
Z321

2
Z19
Z20

4
34H2BJS6N
PIM12MD7RCOLWW09
PYF1J14TF
FIPJOTEA5

5
ABCDE
BCDEF
ABCDA
BAAAA
ACAAA
"""