n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## 서로 겹치지 않는 두 직사각형.
## 두 직사각형 안에 정수 값들의 총 합을 최데
# 직사각형은 크기 탐색?


### 두 좌표가 주어졌을때, 해당 좌표의 직사각형 합
def rec(tl, br):
    x1, y1 = tl
    x2, y2 = br

    count = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            count += grid[i][j]

    return count


### 두 직사각형의 시작 좌표 완전 탐색
### 두 직사각형의 크기 완전 탐색, 모서리를 활용

max_count = -float('inf')
for i in range(n):
    for j in range(m):
        for r in range(n):
            for c in range(m):

                ###########################
                # 첫번째 직사각형 크기 탐색 #
                ###########################

                ## 상단 왼쪽은 시작점 
                tl = (i, j)
                
                ## 하단 오른쪽은 탐색
                for br_i in range(i+1, n+1):
                    for br_j in range(j+1, m+1):
                        
                        ### 첫번째 직사각형 좌표
                        br = (br_i, br_j)

                        ### 첫번째 직사각형의 합 계산
                        first_rec_count = rec(tl, br)


                ############################
                # 두 번째 직사각형 크기 탐색 #
                ############################ 

                        tl_2 = (r, c)
                        
                        for br_2_i in range(r+1, n+1):
                            for br_2_j in range(c+1, m+1):

                                ## 두번째 직사각형 ㅘ표
                                br_2 = (br_2_i, br_2_j)

                                ### 겹치는지 확인

                                if not (br_i <= r or br_j <= c):
                                    if not (br_2_i <= i or br_2_j <= j):
                                        continue

                                # print(tl, br, 'next ',tl_2, br_2)
                                second_rec_count = rec(tl_2, br_2)
                        
                                
                                max_count = max(max_count, first_rec_count + second_rec_count)

print(max_count)






