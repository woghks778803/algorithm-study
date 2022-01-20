# 실버4
# 좋은 단어
if __name__ == "__main__":
    N = int(input())
    result = 0

    for _ in range(N):
        keyword = list(input())
        arr = []

        while keyword:
            keyword_pop = keyword.pop()
            if not arr:
                arr.append(keyword_pop)
            else:
                arr_pop = arr.pop()
                if keyword_pop != arr_pop:
                    arr.append(arr_pop)
                    arr.append(keyword_pop)
                    
        if not arr: result += 1
    print(result)

"""
3
ABAB
AABB
ABBA

3
AAA
AA
AB
"""