# 골드4
# 수 묶기
if __name__ == "__main__":
    N = int(input())
    plus = []
    minus = []
    result = []
    for _ in range(N):
        add = int(input())
        if add == 1:
            result.append(add)
        elif add > 0:
            plus.append(add)
        else:
            minus.append(add)

    minus.sort(reverse=True)
    while len(minus)>1:
        result.append(minus.pop()*minus.pop())

    if len(minus)==1: result.append(minus[0])

    plus.sort()
    while len(plus)>1:
        result.append(plus.pop()*plus.pop())
    if len(plus)==1: result.append(plus[0])
    
    print(sum(result))
    print(result)

"""
5
-2
-1
2
1
3

6
0
1
2
4
3
5

1
-1

3
-1
0
1

2
1
1
"""

