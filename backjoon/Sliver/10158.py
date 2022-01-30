# 실버4
# 개미
if __name__ == "__main__":
    w, h = map(int, input().split())
    p, q = map(int, input().split())
    t = int(input())
    if ((t+p)//w) % 2 == 0: x = (t+p) % w
    else: x = w - ((t+p) % w)

    if ((t+q)//h) % 2 == 0: y = (t+q) % h
    else: y = h - ((t+q) % h)

    print(x, y)
    print(((t+p)//w) % 2, ((t+q)//h) % 2)
    

"""
6 4
4 1
8
"""
        



