n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## 같은 정수면 하나의 블럭, 4개 이상인 경우 블럭이 터짐.
## 터지게 되는 블럭 갯수, 가장 큰 블럭의 크기.

dx_list = [0, 0, 1, -1]
dy_list = [1, -1, 0, 0]


### 모든 그리드 완전 탐색
### 방문하지 않은 노드면 dfs
### 블락 수 count
### dfs 끝났을 시 4 이상이면 터짐 카운트 +=1
### max count 기록

def dfs(r,c):
    global count, cur_num

    if cur_num != grid[r][c]:
        return

    if visited[r][c]:
        return

    visited[r][c] = True
    count += 1

    for dx, dy in zip(dx_list, dy_list):
        nr, nc = r+dx, c+dy
        if 0 <= nr < n and 0 <= nc < n:
            dfs(nr, nc)




visited = [[False] * n for _ in range(n)]
answer=0
boom_count = 0

for i in range(n):
    for j in range(n):
        
        count = 0
        if not visited[i][j]:
            cur_num = grid[i][j]
            dfs(i,j)
    
        if count >= 4:
            boom_count += 1
        answer = max(answer, count)

print(boom_count, answer)