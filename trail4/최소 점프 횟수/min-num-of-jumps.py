n = int(input())
num = list(map(int, input().split()))

# Please write your code here.


# 각 위치로부터 최대 점프 가능 거리 N
# 첫 번째 위치로부터 N번쨰 위치에 도달하기 위해 필요한 최소 점프 횟수.


### dfs 백트랙킹.
### for i in range(1, N): 


min_count = float('inf')
def dfs(count, position):
    global min_count
    if position >= n-1:
        min_count = min(min_count, count)
        return

    
    cur_jump = num[position]

    for i in range(1, cur_jump+1):
        
        position += i
        count += 1
        dfs(count, position)
        count -= 1
        position -= i





dfs(0,0)
if min_count == float('inf'):
    print(-1)
else:
    print(min_count)