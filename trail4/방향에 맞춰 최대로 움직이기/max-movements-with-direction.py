n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
# Please write your code here.

## NxN 에서 방향 정수.
## 특정 위치에서 시작해서 현재 위치에 적혀있는 방향에 있는 수들 중 현재 수 보다 더 큰 수가 적혀있는 곳으로 이동하는 것을 최대한 반복.

## r,c에서 시작해서 최대 몇번 이동할 수 있는지.


## move dir로 끝까지 이동하면서 backtracking.


direction = [
    (-1, 0), # 1
    (-1, 1), # 2
    (0, 1), # 3
    (1, 1), # 4
    (1, 0), # 5
    (1, -1), # 6
    (0, -1), # 7
    (-1, -1) # 8
]

max_count = 0
def dfs(r, c, prev_num, count):
    global max_count
    # cur_num = num[r][c]

    # if prev_num >= cur_num:
    max_count = max(count, max_count)
        # return
    

    move = move_dir[r][c]
    dr, dc = direction[move-1]

    for i in range(n+1):
        if not(0 <= r+dr < n and 0 <= c+dc < n):
            break
        
        cur_num_ = num[r][c]


        r += dr
        c += dc
        

        next_num = num[r][c]


        if prev_num < next_num:
            count += 1
            dfs(r, c, next_num, count)
            count -= 1




dfs(r,c,num[r][c], 0)
print(max_count)
