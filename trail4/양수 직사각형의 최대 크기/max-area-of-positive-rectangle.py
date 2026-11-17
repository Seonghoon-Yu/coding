n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

### 가능한 양끝 좌표
### 양끝 좌표 내 값들이 양수인지 set
### 맞다면 max_area

max_area = -1

for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):

                ### 상자 안의 좌표들 get
                element = set()

                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        element.add(grid[x][y])
                
                check = [0 < e for e in element]
                if not False in check:
                    # print('x2', x2, 'x1', x1)
                    current_area = ((x2+1)-(x1)) * ((y2+1)-(y1))
                    max_area = max(max_area, current_area)

print(max_area)