n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

'''
### 중심과의 거리 문제 풀이
for i in range(n):
    for j in range(n):

        ### 마름모 구간 확인
        for k in range(2*n-1): # 마름모 깊이 범위
            
            sum_k = 0
            ### 중심에서 모든 격자 확인
            for r in range(n):
                for c in range(n):
                    if (abs(r-i) + abs(c-j)) <= k:
                        sum_k += grid[r][c]
                        
            values = sum_k * m
            cost = k**2 + (k+1)**2

            total_cost = values - cost
            if total_cost >= 0:
                max_value = max(max_value, sum_k)

print(max_value)
'''


####### dx, dy 활용하는 풀이
def is_range(i,j):
    # if i >= n or j >=n: ######## 0보다 작으면 못잡음.
    #     return False
    return 0 <= i < n and 0 <= j < n
    
max_value = 0

# 중심점
for i in range(n):
    for j in range(n):



        ### 대각선 이동방향
        dx = [1, 1, -1, -1]
        dy = [-1, 1, 1, -1]

        gold_count = 0
        gold_count += grid[i][j]
        ## 마름모
        for k in range(2 * (n-1) +1):



            ## k번째 마름모에서 가격

            curr_x = i-k
            curr_y = j
            for d in range(4): ## 4번 이동
                
                ### k 만큼 이동
                for _ in range(k):

                    # print(is_range(curr_x, curr_y))
                    if is_range(curr_x, curr_y):
                        gold_count += grid[curr_x][curr_y]

                    curr_x += dx[d]
                    curr_y += dy[d]

            # print(gold_count)

            cost = k**2 + (k+1) **2
            gold_value = gold_count * m
            loss = gold_value - cost
            if loss >= 0:
                max_value = max(max_value, gold_count)

print(max_value)
                    
            









