# 실버1
# 이진 검색 트리
def postOrder(start, end):
    if start > end: return
    
    idx = end + 1

    for i in range(start+1, end+1):
        if arr[i] > arr[start]:
            idx = i
            break
    
    postOrder(start+1, idx-1)
    postOrder(idx, end)
    print(arr[start])

if __name__ == "__main__":  
    import sys
    sys.setrecursionlimit(10**6) # 백준 런타임에러
    arr = list(map(int, sys.stdin.readlines()))
    postOrder(0, len(arr)-1)


# 스택을 이용한 탐색
# def check_left(root, node):
#     if graph[root][0] == None:
#         graph[root][0] = node
#     else:
#         if graph[root][0] > node:
#             check_left(graph[root][0], node)
#         else:
#             check_right(graph[root][0], node)

# def check_right(root, node):
#     if graph[root][1] == None:
#         graph[root][1] = node
#     else:
#         if graph[root][1] > node:
#             check_left(graph[root][1], node)
#         else:
#             check_right(graph[root][1], node)

# def postOrder(root):
#     if root == None: return 0

#     postOrder(graph[root][0])
#     postOrder(graph[root][1])
#     print(root)


# if __name__ == "__main__":  
#     import sys
#     sys.setrecursionlimit(10**6) # 백준 런타임에러
#     arr = list(map(int, sys.stdin.readlines()))
#     graph = {}

#     for node in arr: graph[node] = [None, None]

#     root = None
#     for node in arr: 
#         if root == None:
#             root = node
#         else:
#             if node < root:
#                 check_left(root, node)
#             else:
#                 check_right(root, node)

#     postOrder(root)


# 클래스를 이용한 탐색
# class BinaryTree:
#     node = None
#     l_node = None
#     r_node = None

#     def __init__(self, node=None) -> None:
#         self.node = node

#     def find_postorder(self):
#         if self.l_node != None:
#             self.l_node.find_postorder()
#             sys.stdout.write(str(self.l_node.node)+"\n")

#         if self.r_node != None:
#             self.r_node.find_postorder()
#             sys.stdout.write(str(self.r_node.node)+"\n")

#     def check_left(self, node):
#         if self.l_node == None:
#             self.l_node = BinaryTree(node)
#         else:
#             if self.l_node.node > node:
#                 self.l_node.check_left(node)
#             else:
#                 self.l_node.check_right(node)
    
#     def check_right(self, node):
#         if self.r_node == None:
#             self.r_node = BinaryTree(node)
#         else:
#             if self.r_node.node > node:
#                 self.r_node.check_left(node)
#             else:
#                 self.r_node.check_right(node)

# if __name__ == "__main__":  
#     import sys
#     sys.setrecursionlimit(10**6) # 백준 런타임에러
#     arr = list(map(int, sys.stdin.readlines()))

#     bt = BinaryTree()
#     for node in arr:
#         if bt.node == None:
#             bt.node = node
#         else:
#             if bt.node > node:
#                 bt.check_left(node)
#             else:
#                 bt.check_right(node)

#     bt.find_postorder() 
#     sys.stdout.write(str(bt.node)+"\n")


"""
50
30
24
5
28
45
98
52
60

"""