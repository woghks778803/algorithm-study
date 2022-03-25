# 실버3
# 쇠막대기
# X
S = list(input())
graph = []

for i in range(len(S)):
    if S[i-1] == "(" and S[i] == ")":
        graph.pop()
        graph.append("*")
    else:
        graph.append(S[i])

cnt = 0
result = 0
for i in graph:
    if i == '(':
        cnt += 1
    elif i == ')':
        cnt -= 1
        result += 1
    elif i == '*':
        result += cnt

print(result)
print(graph)

"""
()(((()())(())()))(())
(((()(()()))(())()))(()())
"""