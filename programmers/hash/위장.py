# 위장
# import itertools

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["a", "b"]]

clothes_sort = {}
for i in range(len(clothes)):
    if clothes_sort.get(clothes[i][1]):
        clothes_sort[clothes[i][1]].append(clothes[i][0])
    else:
        clothes_sort[clothes[i][1]] = [clothes[i][0]]

clothes_sort_list = []
for i in clothes_sort:
    clothes_sort_list.append(clothes_sort[i])

result = 1
for i in clothes_sort:
    result = result * (len(clothes_sort[i])+1)
    # combinations_clothes = itertools.combinations(clothes_sort_list, i+1)
    # for j in combinations_clothes:
    #     temp_list = list(j)
    #     result += len(list(itertools.product(*temp_list)))

print(result-1)

