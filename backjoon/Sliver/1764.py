# 실버4
# 듣보잡
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    output = sys.stdout.write

    N, M = map(int, input().split())

    listen = [input().strip() for _ in range(N)]
    look = [input().strip() for _ in range(M)]
    intersection = set(listen) & set(look)

    intersection = sorted(intersection)

    print(len(intersection))
    for i in intersection: output(i+"\n")

"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

2 2
a
aa
a
aa

4 5
fdd
abc
dew
cdc
aa
cdc
fdd
abc
ghd
"""