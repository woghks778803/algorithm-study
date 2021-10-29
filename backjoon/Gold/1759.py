# 골드5
# 암호 만들기
from itertools import combinations

L, C = map(int,input().split())
test_case = input().split()
test_case.sort()
mo = ['a', 'e', 'i', 'o', 'u']

def intersect(list1, list2):
    return list(set(list1) & set(list2))

result = list(combinations(test_case, L))
for i in reversed(range(len(result))):
    if intersect(result[i], mo) == []:
        del result[i]
    elif L - len(intersect(result[i], mo)) < 2 :
        del result[i]

for str_chars in result:
    result_str = ""
    for str_char in str_chars:
        result_str += str_char
    print(result_str)

# 반례

# 3 4
# a t c i

# 3 5
# a t c i s 

