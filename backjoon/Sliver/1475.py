# 실버5
# 방 번호
from collections import Counter
import math
N = list(input())
counter = Counter(N)

result = 0
if counter.get('6'): result += counter['6']
if counter.get('9'): result += counter['9']
result = math.ceil(result/2)

for i in counter:
    if i != '6' and i != '9' and counter[i] > result:
        result = counter[i]

print(result)
print(counter)

# 1567993
# 1452239692