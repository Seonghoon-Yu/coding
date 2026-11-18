n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]


# =========================================================
# 한 도둑이 확보한 M개의 물건 중
# 일부를 골라서
#
# 1) 무게 합이 c 이하이고
# 2) 가치의 합(각 무게의 제곱합)이 최대가 되도록
#
# 최대 가치를 반환하는 함수
# =========================================================

def get_max_value(items):
    max_value = 0

    def dfs(index, weight_sum, value_sum):
        nonlocal max_value

        if index == m:
            max_value = max(max_value, value_sum)
            return
        
        cur_item = items[index]

        ## 현재 아이템을 골라도 무게를 초과하지 않을시에 선택
        if weight_sum + cur_item <= c:
            dfs(index+1, weight_sum + cur_item, value_sum + cur_item * cur_item)

        ## 현재 아이템을 고르지 않은 경우
        dfs(index+1, weight_sum, value_sum)
    dfs(0,0,0)
    return max_value
        
## 모든 가능한 M칸 구간에 대해 최대 가치 미리 계산
profit = [[0] * (n - m + 1) for _ in range(n)]

for i in range(n):
    for j in range(n-m+1):
        items = weight[i][j:j+m]
        profit[i][j] = get_max_value(items)



# =========================================================
# 이제 도둑 2명이 차지할 구간 2개를 고른다
# =========================================================

answer = 0

for r1 in range(n):
    for c1 in range(n-m+1):
        for r2 in range(n):
            for c2 in range(n-m+1):

                if r1 == r2:
                    if not(
                        c1 + m <= c2
                        or
                        c2 + m  <= c1
                    ):
                        continue
                    
                
            
                value1 = profit[r1][c1]
                value2 = profit[r2][c2]


                # 두 도둑이 얻는 가치의 합
                current_value = value1 + value2


                # 전체 최대값 갱신
                answer = max(answer, current_value)


print(answer)


# # ---------------------------------------------------------
# # 첫 번째 도둑의 시작 좌표
# # ---------------------------------------------------------
# for r1 in range(n):

#     for c1 in range(n - m + 1):


#         # -------------------------------------------------
#         # 두 번째 도둑의 시작 좌표
#         # -------------------------------------------------
#         for r2 in range(n):

#             for c2 in range(n - m + 1):


#                 # =================================================
#                 # 두 구간이 겹치는지 검사
#                 # =================================================

#                 # 서로 다른 행이면 절대로 겹치지 않음
#                 #
#                 # 예:
#                 #
#                 # 0행: A A A . .
#                 # 1행: . B B B .
#                 #
#                 # 행 자체가 다르니까 상관없음
#                 if r1 == r2:

#                     # 같은 행일 때만 열 구간 겹침 검사
#                     #
#                     # 구간1:
#                     # c1 ~ c1 + m - 1
#                     #
#                     # 구간2:
#                     # c2 ~ c2 + m - 1


#                     # 안 겹치는 경우는 둘 중 하나:
#                     #
#                     # 1) 구간1이 구간2보다 완전히 왼쪽
#                     #    c1 + m <= c2
#                     #
#                     # 2) 구간2가 구간1보다 완전히 왼쪽
#                     #    c2 + m <= c1
#                     #
#                     # 둘 다 아니면 겹친 것
#                     if not (
#                         c1 + m <= c2
#                         or
#                         c2 + m <= c1
#                     ):
#                         continue


#                 # =================================================
#                 # 겹치지 않는 두 구간이면
#                 # 각 구간의 최대 가치는 이미 profit에 있음
#                 # =================================================

#                 value1 = profit[r1][c1]
#                 value2 = profit[r2][c2]


#                 # 두 도둑이 얻는 가치의 합
#                 current_value = value1 + value2


#                 # 전체 최대값 갱신
#                 answer = max(answer, current_value)


# print(answer)