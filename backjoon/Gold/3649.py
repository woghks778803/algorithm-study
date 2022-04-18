# 골드4
# 로봇 프로젝트
import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())*10000000
        n = int(input())

        result = []
        T = {}
        for _ in range(n):
            num = int(input())
            if T.get(x-num): 
                result.append([num, x-num, abs(num-(x-num))])
            else: 
                T[num] = True

        if not result:
            print("danger")
        else:
            result.sort(key= lambda l : abs(l[2]) )
            bg, sm, c = result.pop()
            if sm > bg:
                temp = bg
                bg = sm
                sm = temp

            print(f"yes {sm} {bg}")
    except:
        break

"""
1
4
9999998
1
2
9999999
"""