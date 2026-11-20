n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


## 완전 탐색.
## 모든 마름모 직사각형 해보고 해당 grid sum max가 되는걸로 하면 됌.


directions = [
    (-1, 1),
    (-1, -1),
    (1, -1),
    (1, 1)
]

max_count = 0

for i in range(n):
    for j in range(n):
        ## 시작점
        ## 각 방향대로 n번 반복
            
        for h in range(1, n+3):
            for w in range(1, n+3):
                h_w = [h,w,h,w]
                
                nx, ny = i, j
                    
                count = 0
                possible = True
                
                for (dx, dy), k in zip(directions, h_w):

                    for _ in range(k):
                        nx, ny = nx+dx, ny+dy


                        ## nx, ny가 벗어났는지 확인
                        if not (0 <= nx < n and 0 <= ny < n):
                            possible = False
                            break
                        if possible:
                            count += grid[nx][ny]
                    
                if possible:
                    max_count = max(max_count, count)

print(max_count)



