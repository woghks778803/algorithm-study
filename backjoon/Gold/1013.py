# 골드5
# Contact
import re
for i in range(int(input())):
    S = input()
    comp = re.compile("(100+1+|01)+")
    result = re.fullmatch(comp, S)

    if result and result.group() == S:
        print("YES")
    else:
        print("NO")
    
"""
3
10010111
011000100110001
0110001011001

4
100111001
011000110101
1010010101
110001000101
"""