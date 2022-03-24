# 실버4
# 매직 스퀘어로 변경하기
# X
def chk():
    r = S[0]+S[1]+S[2]
    for i in range(3, 7, 3):
        c_r = S[0+i]+S[1+i]+S[2+i]
        if r != c_r: return False
    
    c = S[0]+S[3]+S[6]
    for i in range(1, 3, 1):
        c_c = S[0+i]+S[3+i]+S[6+i]
        if c != c_c: return False

    if S[0]+S[4]+S[8] != S[2]+S[4]+S[6]:
        return False
    
    return True

def simulation(pos):
    if pos == 9:
        if chk():
            calc = 0
            for i in range(9): calc += abs(A[i] - S[i])
            global MIN
            MIN = min(MIN, calc)
        
        return
    
    for i in range(1, 10):
        if not use[i]:
            use[i] = True
            S[pos] = i
            simulation(pos+1)
            use[i] = False
            S[pos] = 0


if __name__ == "__main__":    
    MIN = int(1e32)
    S = [0 for _ in range(9)]
    use = [False for _ in range(10)]
    A = []
    for _ in range(3):
        A.extend([int(i) for i in input().split()])

    simulation(0)
    print(MIN)



"""
4 9 2
3 5 7
8 1 5

4 8 2
4 5 7
6 1 6

1 7 4
2 5 4
3 7 4

5
6
7
14

3
2
1
6

2
1
0
7

4
3
2
5
"""