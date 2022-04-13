# 실버5
# DNA
N, M = map(int, input().split())
T = [list(input()) for _ in range(N)]

arr = []
cnt = 0

for i in range(M):
    str_cnt = {}
    for j in range(N):
        p = T[j][i]
        if str_cnt.get(p): str_cnt[p] += 1
        else: str_cnt[p] = 1

    lst = list(str_cnt.items())
    lst.sort(key= lambda x : (-x[1], x[0]))

    arr.append(lst[0][0])
    cnt += N-lst[0][1]

print("".join(arr))
print(cnt)


"""
5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT

4 10
ACGTACGTAC
CCGTACGTAG
GCGTACGTAT
TCGTACGTAA
"""