# 실버4
# 국영수
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    output = sys.stdout.write
    N = int(input())

    lst = []
    for _ in range(N):
        name, k, m, e = map(str, input().split())
        lst.append([name, int(k), int(m), int(e)])

    lst.sort(key= lambda x : (-x[1], x[2], -x[3], x[0]))
    for i in lst: output(i[0]+'\n')
    # print(lst)
"""
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""