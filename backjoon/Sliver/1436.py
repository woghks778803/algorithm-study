# 실버5
# 영화감독 숌
def movie_title(n):
    i = 0
    cnt = 0
    while True:
        i += 1
        j = str(i)
        if j.count("666") >= 1:
            # print(j)
            title = i
            cnt += 1
        if cnt == n:
            break
    return title

n = int(input())
print(movie_title(n))

"""
1
= 666
2
= 1666
120
= 65666
187
= 66666
400
= 165666
500
= 166699
1801
= 666000
5500
= 1665666
6500
= 1666999
"""

# 성능업
# N = int(input())

# count = 1
# ln = 0
# rn = 0
# out_ln = ""
# out_rn = 0
# mid = 666
# position = 1

# while N > 1:
#     if position == 1:
#         ln += 1
#         out_ln = str(ln)
#         if ln % 10 == 6:
#             position = 2
#             rn = 0
#             if ln % 10000 == 6666:
#                 out_ln = "" if ln//10000 == 0 else str(ln//10000)
#                 out_rn = "000"+str(rn)
#             elif ln % 1000 == 666:
#                 out_ln = "" if ln//1000 == 0 else str(ln//1000)
#                 out_rn = "00"+str(rn)
#             elif ln % 100 == 66:
#                 out_ln = "" if ln//100 == 0 else str(ln//100)
#                 out_rn = "0"+str(rn)
#             else:
#                 out_ln = "" if ln//10 == 0 else str(ln//10)
#                 out_rn = str(rn)
#     else:
#         rn += 1
#         if ln % 10000 == 6666:
#             if rn < 10:
#                 out_rn = "000"+str(rn)
#             elif rn < 100:
#                 out_rn = "00"+str(rn)
#             elif rn < 1000:
#                 out_rn = "0"+str(rn)
#             else:
#                 out_rn = str(rn)

#             if rn == 10000:
#                 ln += 1
#                 out_ln = str(ln)
#                 position = 1
#         elif ln % 1000 == 666:
#             if rn < 10:
#                 out_rn = "00"+str(rn)
#             elif rn < 100:
#                 out_rn = "0"+str(rn)
#             else:
#                 out_rn = str(rn)
            
#             if rn == 1000:
#                 ln += 1
#                 out_ln = str(ln)
#                 position = 1
#         elif ln % 100 == 66:
#             if rn < 10:
#                 out_rn = "0"+str(rn)
#             else:
#                 out_rn = str(rn)

#             if rn == 100:
#                 ln += 1
#                 out_ln = str(ln)
#                 position = 1
#         elif ln % 10 == 6:
#             out_rn = str(rn)

#             if rn == 10:
#                 ln += 1
#                 out_ln = str(ln)
#                 position = 1
#     count += 1
#     if count == N:
#         break

# if position == 1:
#     print(str(out_ln)+str(mid))
# else:
#     print(str(out_ln)+str(mid)+str(out_rn))