# 실버3
# 서로 다른 부분 문자열의 개수

if __name__ == "__main__":
    S = input()
    result = dict()

    for i in range(len(S)):
        for j in range(i, len(S)):
            result[S[i:j+1]] = True

    print(len(result))
    # print(result)

'''
ababc
'''