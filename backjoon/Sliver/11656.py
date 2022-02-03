# 실버4
# 접미사 배열
if __name__ == "__main__":
    S = list(input())
    result = []
    for i in range(len(S)): result.append("".join(S[i:len(S)]))
    result.sort()
    for s in result: print(s)

"""
baekjoon
jaehwan
"""