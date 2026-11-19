from collections import deque, defaultdict

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

### 이동경로상 모든 칸에 적힌 정수가 x보다 적어야 한다.
# 특정 위치에서 시작해서 조건을 만족하는 위치를 찾아 상하좌우만 이동,
#  그리고 K번 반복한 이후의 위치.
# 조건 1. 무조건 출발 정수보다 작아야하고, 이동 경로도 x보다 작음. 이렇게 이동 가능한 곳.
# 조건 2. 1번 만족할 수 있는 칸중에 정수 중 최댓값
# 조건 3. 2번 만족하는게 여러개인 경우 행번호가 가장 작은곳.
# 조건 4. 조건3 이 여러개인경우 열 번호가 작은곳.

# 다음 위치에서도 다음 최댓값 인 조건 반복.
# K번 반복 후 최종 위치. 더 이상 새로 이동할 위치가 없다면 움직이는 것을 종료.


###### 방문하는 값마다 좌표를 dictionary에 저장?
### BFS를 K번 반복

directions = [(0,1), (0,-1), (1,0), (-1,0)]


### 중간중간 들리면서 max check하면서 시작점보다 작은거 check
### 나중에 dict에서 max값 꺼내와서 좌표 비교

def bfs(r, c):
    queue = deque()
    queue.append((r,c))

    visited[r][c] = True

    start_val = grid[r][c]

    best_r, best_c = -1, -1

    while queue:
        
        sr, sc = queue.popleft()

        for dr, dc in directions:
            nr, nc = sr+dr, sc+dc

            if not (0 <= nr < n and 0 <= nc < n):
                continue
            
            if visited[nr][nc]:
                continue
            
            if start_val <= grid[nr][nc]:
                continue
            
            visited[nr][nc] = True
            queue.append((nr,nc))


            ## 현재 best가 없다면
            if best_r == -1 and best_c == -1:
                best_r, best_c = nr, nc
            else:
                if grid[best_r][best_c] < grid[nr][nc]: # best 보다 크면
                    best_r, best_c = nr, nc

                elif grid[best_r][best_c] == grid[nr][nc]: # 같으면
                    ###
                    if best_r > nr:
                        best_r = nr
                        best_c = nc
                    if best_r == nr and best_c > nc:
                        best_r = nr
                        best_c = nc

    if best_r == -1 and best_c == -1:
        return None

    return (best_r, best_c)

            

            



r -= 1
c -= 1

for _ in range(k):
    visited = [[False] * n for _ in range(n)]
    next_pos = bfs(r, c)

    if next_pos == None:
        break
    r, c = next_pos

print(r+1, c+1)
