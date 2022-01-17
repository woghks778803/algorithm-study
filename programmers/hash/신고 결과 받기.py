def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    cnt = [0 for i in range(len(id_list))]
    graph = {}
    
    for i in report:
        a, b = i.split()
        if graph.get(a):
            if graph.get(a).get(b):
                pass
            else:
                graph[a][b] = True
                cnt[id_list.index(b)] += 1
        else:
            graph[a] = {b:True}
            cnt[id_list.index(b)] += 1

    for name in id_list:
        if graph.get(name):
            for r in graph[name]:
                if cnt[id_list.index(r)] >= k: answer[id_list.index(name)] += 1
    
    return answer