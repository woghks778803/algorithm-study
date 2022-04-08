# 실버5
# 폴리오미노
S = list(input())
DP = ["", -1, "BB", -1]
cnt = []
fail_chk = False

prev = True
for s in S:
    if s == ".":
        prev = True
        cnt.append(0)
    else:
        if prev:
            prev = False
            cnt.append(0)

        cnt[-1] += 1

result = []
for c in cnt:
    if c == 0:
        result.append(".")
    else:
        if DP[c%4] == -1:
            fail_chk = True
            break

        result.append((c//4*"AAAA")+DP[c%4])

if fail_chk: print(-1)
else: print("".join(result))

"""
XXXX....XXX.....XX
XX.XXXXXXXXXX..XXXXXXXX...XXXXXX
XX.XXXXXXXXXXXXXXXXXXXXXXXXXX....XX.XXXX.XXXX.XXXX.
"""