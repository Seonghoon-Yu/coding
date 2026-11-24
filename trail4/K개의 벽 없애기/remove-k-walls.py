n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.

## K 개 벽을 적절하게 없애서 최소 시간


## 모든 가능한 k를 없애는 경우의 수 

## 완전 탐색으로 벽을 없애는 point 경우의 수.

removed = []
all_possible = False
answer = float('inf')
def dfs(index, removed):
    global all_possible, answer, visited, c_map

    if len(removed) == k:
        for r, c in removed:
            grid[r][c] = 0

        visited = [[False] * n for _ in range(n)]
        c_map = [[0] * n for _ in range(n)]
        
        bfs()

        if visited[r2][c2]:    
            all_possible=True
            
            answer = min(c_map[r2][c2], answer)


        for r, c in removed:
            grid[r][c] = 1
        return
    
    for i in range(index, n*n):
        r = i // n
        c = i % n

        if grid[r][c] == 1:
            removed.append((r,c))
            dfs(i+1, removed)
            removed.pop()    


def bfs():
    global visited
    from collections import deque
    block = [
        (1,0),
        (-1,0),
        (0,-1),
        (0,1)
    ]
    
    queue = deque()
    queue.append((r1,c1))

    visited[r1][c1] = True

    possible=False
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in block:
            nr, nc = r+dr, c+dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append((nr, nc))
                c_map[nr][nc] = c_map[r][c] + 1
                if nr == r2 and nc == c2:
                    possible=True

                    return possible

    return possible

dfs(0,[])

if all_possible:
    print(answer)
else:
    print(-1)