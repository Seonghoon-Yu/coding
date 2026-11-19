n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]


graph = [[] for _ in range(n+1)]

### 그래프 제작
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)


### 방문 확인
visited = [False for _ in range(n+1)]


## dfs
def dfs(index):
    visited[index] = True

    ### 그래프에서 index에 해당하는 노드의 간선 하나씩 꺼내보기
    for next_node in graph[index]:
        if not visited[next_node]:
            dfs(next_node)

dfs(1)

print(sum(visited)-1)