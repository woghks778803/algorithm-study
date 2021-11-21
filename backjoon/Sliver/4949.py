# 실버4
# 균형잡힌 세상
import sys

while True:
    T = list(sys.stdin.readline().replace("\n",""))
    
    if len(T) == 1 and T[0] == ".": break
    
    list1 = []
    list2 = []
    for i in range(len(T)):
        if T[i] == "(" or T[i] == ")" or T[i] == "[" or T[i] == "]":
            list1.append(T[i])

    for i in range(len(list1)):
        pop_item = list1.pop()
        
        if list2:
            pop_item2 = list2.pop()
            if (pop_item == "(" and pop_item2 == ")") or (pop_item == "[" and pop_item2 == "]"): 
                pass
            else: 
                list2.append(pop_item2)
                list2.append(pop_item)
        else:
            list2.append(pop_item)

    if list2: print("no")
    else: print("yes")



"""
([())]
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
"""