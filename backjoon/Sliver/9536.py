# 실버4
# 여우는 어떻게 울지?
T = int(input())

for i in range(T):
    sentence = input().split()
    graph = {}
    while True:
        command = input()
        if command == "what does the fox say?": break

        c = command.split()
        graph[c[2]]= c[0]

    result = []
    while sentence:
        i = sentence.pop()
        if not graph.get(i): result.append(i)

    while result: print(result.pop(), end=" ")



"""
1
toot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot
dog goes woof
fish goes blub
elephant goes toot
seal goes ow
what does the fox say?
"""