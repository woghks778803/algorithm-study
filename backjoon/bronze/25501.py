# 브론즈2
# 재귀의 귀재
# Palindrome
def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    for _ in range(int(input())):
        s = input().strip()
        cnt = 0
        print(isPalindrome(s), cnt)


"""
5
AAA
ABBA
ABABA
ABCA
PALINDROME
"""
