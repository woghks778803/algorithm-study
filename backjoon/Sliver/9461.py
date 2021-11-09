# 실버3
# 파도반 수열
import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    N = int(sys.stdin.readline().strip())
    num_list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    standard = 10
    while True:
        num_list.append(num_list[standard-1] + num_list[standard-5])
        standard += 1
        if standard == 100:
            break

    print(num_list[N-1])

"""
2
6
12
"""