# 실버5
# 셀프넘버
def d(n):
    str_n = str(n)
    for i in range(len(str_n)):
        n += int(str_n[i])
    return n

num_list = [i for i in range(1, 10000)]
n = 0
while n <= 10000:
    n += 1
    result_n = d(n)

    if result_n in num_list:
        num_list.remove(result_n)

for i in num_list:
    print(i)

# num_list = [1, 3, 5]
# num_list.remove(3)
# print(num_list)