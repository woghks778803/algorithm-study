# 실버4
# 괄호
import sys
N = int(sys.stdin.readline())

for i in range(N):
    T = list(sys.stdin.readline().strip())

    r = 0
    l = 0
    for i in T:
        if i == "(": l += 1
        else: r += 1
        
        if r > l: break

    if l != r: print("NO")
    else: print("YES")
"""
반례

6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

3
((
))
())(()
"""