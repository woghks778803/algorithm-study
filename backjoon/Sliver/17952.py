# 실버3
# 과제는 끝나지 않아!
import sys
input = sys.stdin.readline

score = 0
works = []
N = int(input())

for i in range(N):
    data = input().strip()

    if data == "0":
        if works: a, b, c = works.pop()
        else: a = b = c = 0
    else:
        a, b, c = map(int, data.split())

    c -= 1
    if c == 0: score += b
    elif c > 0: works.append([a, b, c])

print(score)

"""
3
1 100 3
0
0

5
1 10 3
0
1 100 2
1 20 1
0

1
1 1 1
"""