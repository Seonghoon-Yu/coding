n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


### 시작지점 0,0에서 4방향 탐색
### 이미 방문한 경로 check
### 뱀 위치를 먼저 visited로? ㄴㄴ 만약에 이동하려는데 뱀 위치면 이동 ㄴ


visited = [[False] * m for _ in range(n)]
block =[
    (1, 0),
    # (-1, 0),
    (0, 1),
    # (0, -1)
]

def dfs(r, c):

    # ######## 종료조건 뭘로?
    # if r == (n-1) and c == (m-1):
    #     return
    
    if grid[r][c] == False: ## 뱀을 만날시
        return

    if visited[r][c] == True: ## 이미 방문한 노드
        return

    visited[r][c] = True # 방문


    ### 4방향 탐색
    for dx, dy in block:
        if 0 <= r+dx < n and 0 <= c+dy < m:
            dfs(r+dx, c+dy)

dfs(0,0)
print(int(visited[n-1][m-1]))


# print(visited)




