# 골드2
# 가운데를 말해요
# X
import sys
import heapq
N = int(sys.stdin.readline().replace("\n", ""))
min_heap = []
max_heap = []
for _ in range(N):
    now = int(sys.stdin.readline().replace("\n", ""))

    # 힙은 이진 트리이므로 중간값을 구하기위해 최소 힙과 최대 힙을 분리(이진 트리처럼)해서
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-1 * now, now))
    else:
        heapq.heappush(min_heap, (now, now))

    # print(max_heap, min_heap)
    # 두 값의 중앙값을 비교한다. 최소 힙의 중앙값보다 최대 힙의 중앙값이 큰 경우 교환
    # 최대 힙은 중앙값이 최솟값 최소 힙은 중앙값이 최댓값
    if min_heap and min_heap[0][1] < max_heap[0][1]:
        temp_a = heapq.heappop(min_heap)[1] # now 값 불러오기
        temp_b = heapq.heappop(max_heap)[1] # now 값 불러오기
        heapq.heappush(min_heap, (temp_b, temp_b))
        heapq.heappush(max_heap, (-1*temp_a, temp_a))
    
    print(max_heap[0][1])


"""
7
1
5
2
10
-99
7
5
"""