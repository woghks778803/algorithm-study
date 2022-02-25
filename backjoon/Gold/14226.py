# 골드5
# 이모티콘
def bfs():
    # 현재 입력 수, 클립 수
    dq = deque([])
    dq.append([1,0])
    DP[1][0] = 0

    while dq:
        dist = dq.popleft()

        # 값 도달시 중지
        if dist[0] == S: 
            print(DP[dist[0]][dist[1]])
            break

        # 제거, 붙여넣기, 복사
        pattern = [-1, dist[1], 0]
        for i in range(3):
            next_cnt = dist[0]+pattern[i]
            if 0 <= next_cnt <= S:
                if i == 2 and DP[next_cnt][dist[0]] == -1: # 복사의 경우
                    DP[next_cnt][dist[0]] = DP[dist[0]][dist[1]]+1
                    dq.append([next_cnt, dist[0]])

                if i != 2 and DP[next_cnt][dist[1]] == -1: # 그외
                    DP[next_cnt][dist[1]] = DP[dist[0]][dist[1]]+1
                    dq.append([next_cnt, dist[1]])


if __name__ == "__main__":
    from collections import deque
    S = int(input())
    DP = [[-1 for _ in range(S+1)] for _ in range(S+1)]
    bfs()



