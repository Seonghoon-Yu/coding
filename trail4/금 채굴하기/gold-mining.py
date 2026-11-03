n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_value = 0

### 중심과의 거리 문제
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







