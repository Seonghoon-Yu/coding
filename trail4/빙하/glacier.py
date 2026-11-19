n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## 바깥물 grid
## True와 맞닿아 있는 얘들은 다음에 0으로 변경
## 매번 다음에 all 0이 되는지 확인하고 다음에 변경이 all 0 이면 이전값에서 1 all sum


### 그러면 바깥물 grid를 매 초 마다 bfs로 결정하고
### 바깥물을 순회하면서 인접한 물들 다 0으로 만든 Next grid 만들고
## next grid가 all 0인지 확인하고 아니라면 1초 더 돌고
## next grid가 all 0이면, 이전 grid에서 남아있는 1 다 sum


out_water = [[False] * m for _ in range(n)]

### 0번부터 bfs로 바깥물 확인

def update_out_water():
    from collections import deque

    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0,0))

    visited[0][0] = True
    out_water[0][0] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r+dr, c+dc

            ## grid = 1 이라면 탐색 x
            ## grid ==[0] 이라면 True

            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc]:
                    if grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        out_water[nr][nc] = True

                        queue.append((nr, nc))


## next grid
def next_grid():
    from collections import deque

    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0,0))

    visited[0][0] = True

    while queue:
        r, c = queue.popleft()

        ## out_water의 True 부분을 순회 해야함.
        if out_water[r][c]:
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc]:
                        grid[nr][nc] = 0

                        visited[nr][nc] = True

                        queue.append((nr,nc))
            

def check_grid(grid):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return False

    return True

for t in range(100):
    ## out_water 확인
    update_out_water()

    ## outwater 인접한 grid 다 0으로 만들기
    prev_grid = [r[:] for r in grid]
    next_grid() # grid update

    if check_grid(grid): ## True면 다 녹ㅇ,ㅁ
        break

count = 0
for i in range(n):
    for j in range(m):
        if prev_grid[i][j] == 1:
            count += 1

print(t+1, count)

