n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]


graph = [[] for _ in range(n+1)]

for i, j in edges:
    ## 양방향 연결
    graph[i].append(j)
    graph[j].append(i)


visited = [False for _ in range(n+1)]


def dfs(index):

    visited[index] = True

    for next_node in graph[index]:
        if not visited[next_node]:
            dfs(next_node)


dfs(1)
print(sum(visited)-1)