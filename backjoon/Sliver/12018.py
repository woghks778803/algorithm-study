# 실버3
# Yonsei TOTO
N, M = map(int, input().split())

lst = []
for i in range(N):
    p, l = map(int, input().split())
    T = [int(i) for i in input().split()]
    T.sort(reverse=True)

    if p < l: lst.append(1)
    else: lst.append(T[l-1])

result = 0
lst.sort(reverse=True)

while lst:
    M = M-lst.pop()
    if M >= 0: result += 1
    else: break
    
print(result)


"""
5 76
5 4 
36 25 1 36 36
4 4
30 24 25 20
6 4
36 36 36 36 36 36
2 4
3 7
5 4
27 15 26 8 14
"""