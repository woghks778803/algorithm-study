# 골드4
# 소수 경로
# 에라토스테네스의 체
def et_prime(dp):
    for i in range(2, 10000):
        if dp[i] == False:
            if i >= 1000: sosu.append(i) # 1000 이상만 저장
            for j in range(i*2, 10000, i): dp[j] = True
    
    del dp

def bfs(start, end):

    if start == end:
        return 0
    else:
        dq = deque([[start, 1]])
        visited[int(start)] = True
        
        while dq:
            standard, depth = map(str, dq.popleft())
            standard = list(standard)
            
            for s in range(4): # 한번에 한 자릿수만 변경이 되므로 각 자릿수별로 연산
                for i in range(10):
                    if standard[s] != str(i): # 기존값과 비교값이 같으면 패스
                        temp = standard[s] # 기존값 임시저장
                        standard[s] = str(i) # 기존값을 연산을 위해 비교값으로 대체
                        ch = ''.join(standard) # 문자열 연결 

                        if visited[int(ch)] == False: # 방문 체크 - 방문 안한경우만
                            visited[int(ch)] = True 
                            if end == ch:
                                return int(depth) # 최초 발견이 곧 최소횟수
                            elif sosu.count(int(ch)) > 0: 
                                dq.append([ch, int(depth)+1]) 

                        standard[s] = temp # 기존값 복원

if __name__ == "__main__":
    from collections import deque
    N = int(input())
    DP = [False for _ in range(10000)]
    sosu = []
    et_prime(DP)
    
    for i in range(N):
        a, b = input().split()
        visited = [False for _ in range(10000)]
        result = bfs(a, b)

        if result is None: print("Impossible")
        else: print(result)


"""
3
1033 8179
1373 8017
1033 1033
"""