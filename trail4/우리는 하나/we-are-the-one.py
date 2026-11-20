n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## 각 칸마다 도시, 도시 높이, K개 도시를 겹치지 않게 골라서, K개 도시로부터 갈 수 있는 도시 최대화
## 도시간 높이차가 U이상 D 이하.
## 최대 도시.

## 시작점이 K개이고, 고른 K개의 도시로부터 갈 수 있는 도시를 max

## grid 완전 탐색으로 각 지점부터 많이 갈 수 있는 도시 max 인데, 
## 서로 다른 도시라는 조건이 붙음.
## 모든 가능한 좌표 조합을 계산해서, 각 조합으로 K로 visited sum?


### 1. grid에서 모든 가능한 K개의 시작 위치.

possible_k_start_coord = []

def possible_k_start_city(index, count, total):
    if count == k:
        possible_k_start_coord.append(total[:])
        return

    for i in range(index,n*n):
        r = i // n
        c = i % n

        # possible_k_start_coord.append((r,c)
        total.append((r,c))
        possible_k_start_city(i+1, count+1, total)
        total.pop()

possible_k_start_city(0,0,[])

## 2. 모든 K 에서 visited sum 계산.

def bfs(candidates):
    from collections import deque
    
    directions = [(0,1), (0,-1), (1,0), (-1, 0)]
    
    queue = deque()
    
    for r, c in candidates:
        queue.append((r,c))
        visited[r][c] = True
    
    ######## best_r, c
    ######## count


    while queue:
        r, c = queue.popleft()
        cur_height = grid[r][c]
        for dr, dc in directions:
            nr, nc = r+dr, c+dc

            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    ### U, D 확인
                    next_height = grid[nr][nc]

                    if u <= abs(cur_height - next_height) <= d:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
    

max_count = 0


for start_candidates in possible_k_start_coord:
    count = 0
    visited = [[False] * n for _ in range(n)]
    bfs(start_candidates)
    # print(visited)
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                count += 1
    
    max_count = max(max_count, count)

print(max_count)