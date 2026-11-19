n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## 완전 탐색 하면서 사람이 있는 곳을 만나면 DFS
## 그리고 visited

visited = [[False] * n for _ in range(n)]

block = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
]

count = 0

def dfs(r, c):
    global count

    if visited[r][c]:

        return
    # if 0 <= r < n or 0 <= c < n:
    #     answer = max(count, answer)
    #     return

    if not grid[r][c]:
        return

    visited[r][c] = True
    count += 1

    for dx, dy in block:
        if 0 <= r+dx < n and 0 <= c+dy < n:
            dfs(r+dx, c+dy)



viliges = []
## 완전 탐색
for i in range(n):
    for j in range(n):

        if visited[i][j]: # 이미 방문 했으면
            continue
        if grid[i][j]: ## 사람이 살면
            count=0
            dfs(i,j)
            viliges.append(count)

# print(viliges)
print(len(viliges))
viliges.sort()
for v in viliges:
    print(v)