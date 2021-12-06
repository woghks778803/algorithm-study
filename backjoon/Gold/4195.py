# 골드2
# 친구 네트워크
import sys
T = int(sys.stdin.readline())

def root_value_find(r): # root 값 찾기
    r = root_find(r)
    return cnt[r]+1

def union(p, c):
    x = root_find(p)
    y = root_find(c)
    if x == y: return 

    # 작은 집합이 큰 집합 안에 속하도록 변경
    if cnt[x] < cnt[y]: 
        root[x] = y
        cnt[y] += cnt[x]+1
        cnt[x] = 0
    else: 
        root[y] = x
        cnt[x] += cnt[y]+1
        cnt[y] = 0

def root_find(a): # root 찾기
    if root[a] == a: return a
    else: return root_find(root[a])

for _ in range(T):
    F = int(sys.stdin.readline())
    
    root = {}
    cnt = {}

    for _ in range(F):
        a, b = sys.stdin.readline().split()
        
        # 초기값 생성
        if root.get(a): 
            pass
        else: 
            root[a] = a
            cnt[a] = 0

        if root.get(b): 
            pass
        else: 
            root[b] = b
            cnt[b] = 0

        union(a, b)
        print(root_value_find(root[b]))
        # print(p[a])
        # print(root, cnt)


"""
1
8
Fred Barney
Barney Betty
Betty Wilma
Fred Bary
Bey yad
Bey Fred
Betty lma
yad bd

2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty

1
10
a b
b c
c d
d e
e a
f g
g h
i j
j k
g k

1
5
f g
g h
i j
j k
g k
"""
