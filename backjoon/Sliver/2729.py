# 실버5
# 이진수 덧셈
T = int(input())

for _ in range(T):
    a, b = map(list, input().split())
    arr = []
    temp = 0

    while True:

        # a, b가 모두 비었을때
        if not a and not b: 
            if temp == 1: arr.append(temp) # 남은 값이 존재할 경우
            break

        if a: a_num = int(a.pop())
        else: a_num = 0

        if b: b_num = int(b.pop())
        else: b_num = 0

        arr.append((a_num+b_num+temp)%2)
        temp = (a_num+b_num+temp)//2

    # 앞자리 0 제거
    result = []
    leading_zero_chk = True
    while arr:
        r = arr.pop()
        if leading_zero_chk and r==0: continue
        else: leading_zero_chk = False

        result.append(str(r))

    if result: print("".join(result))
    else: print(0)

"""
3
1001101 10010
1001001 11001
1000111 1010110

1
00001110 000101011
=111001

1
10001010 1010101010
=1100110100

1
0 0
"""