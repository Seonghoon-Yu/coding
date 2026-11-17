n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

## 풀이 1: 완전 탐색, 각각 영역에 맞게 pooling

### Transpose는 연산 cost가 높음. 그냥 pooled size가 고정이여서 indexing으로 하는게 나음.
max_values = 0

for i in range(n):
    for j in range(m):

        # ㄴ 모양
        if i < n-1 and j < m-1:
            square = [
                grid[i][j],
                grid[i+1][j],
                grid[i][j+1],
                grid[i+1][j+1]
            ]

            current_max = sum(square) - min(square)
            max_values = max(max_values, current_max)
        
        # ㅡ 모양
        if j < m-2:
            square = [
                grid[i][j],
                grid[i][j+1],
                grid[i][j+2]
            ]

            current_max = sum(square)
            max_values = max(max_values, current_max)
        
        if i < n-2:
            square = [
                grid[i][j],
                grid[i+1][j],
                grid[i+2][j]
            ]

            current_max = sum(square)
            max_values = max(max_values, current_max)

print(max_values)





## 풀이 2: 모양 정해두고 좌표로 보기?

# Please write your code here.
