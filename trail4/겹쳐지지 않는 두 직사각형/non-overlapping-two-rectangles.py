n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


## 1. 직사각형
## i,j 부터 시작해서 모든 가능한 직사각형 check
## 2. 직사각형
## i,j부터 시작해서 1과 겹치지 않는 모든 가능한 직사각형 check

max_sum = -float('inf')

#### 두 직사각형의 첫점과 끝점을 구한다.
#### 두 직사각형 사이의 첫점과 끝점이 overlab 되지 않으면 current sum을 계산한다.

# 첫번째 직사각형 (x1, y1, x2, y2)
# 두번째 직사각형 (x3, y3, x3, y3)

for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                for x3 in range(n):
                    for y3 in range(m):
                        for x4 in range(x3, n):
                            for y4 in range(y3, m):


                                # ## overlab 구하는 법
                                # x_range_1 = [x for x in range(x1, x2+1)]
                                # x_range_2 = [x for x in range(x3, x4+1)]
                                # y_range_1 = [y for y in range(y1, y2+1)]
                                # y_range_2 = [y for y in range(y3, y4+1)]

                                # x_overlab = set(x_range_1) & set(x_range_2)
                                # y_overlab = set(y_range_1) & set(y_range_2)

                                # if x_overlab or y_overlab:
                                #     continue

                                ### 좌표로 overlab 구하는 법
                                current_sum = 0


                                if x2 < x3 or y2 < y3 or x4 < x1 or y4 < y1: # overlab이 없는 경우
                                    ### 첫번째 상자 sum
                                    for cx in range(x1, x2+1):
                                        for cy in range(y1, y2+1):
                                            current_sum += grid[cx][cy]
                                    
                                    for cx in range(x3, x4+1):
                                        for cy in range(y3, y4+1):
                                            current_sum += grid[cx][cy]
                                    
                                    max_sum = max(max_sum, current_sum)

print(max_sum)

    #                             break
    #                         break
    #                     break
    #                 break
    #             break
    #         break
    #     break
    # break
