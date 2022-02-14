# 실버4
# 팰린드롬 만들기
def reverse_print(check):
    global counter
    if check: counter = reversed(counter)
    
    for cnt in counter:
        if odd[0] == cnt[0]:
            if odd[1] > 1: 
                for _ in range((odd[1]-1)//2): print(cnt[0], end="")
        else:
            for _ in range(cnt[1]//2): print(cnt[0], end="")

if __name__ == "__main__":
    from collections import Counter
    name = list(input())
    len_name = len(name)
    counter = Counter(name)
    counter = sorted(counter.items(), key= lambda x : (x[0], x[1]))
    odd = [None, 0, 0] # 홀수 문자, 해당 홀수 문자의 수, 전체 홀수 문자 종류

    for cnt in counter:
        if cnt[1] % 2 == 1: 
            odd[2] += 1
            if odd[0] is None: 
                odd[0] = cnt[0]
                odd[1] = cnt[1]

    if odd[2] < 2:
        reverse_print(False)
        if odd[2] == 1:
            for _ in range(1): print(odd[0], end="")
        reverse_print(True)
    else:
        print("I'm Sorry Hansoo")

# print(name)
# print(counter)
# print(odd)

"""
AABBA
ABACABA
ADBDACCCABA
"""