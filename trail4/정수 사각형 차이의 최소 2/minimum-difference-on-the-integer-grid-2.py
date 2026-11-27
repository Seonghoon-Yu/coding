n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]



INF = float('inf')
answer = INF


values = set()
for i in range(n):
    for j in range(n):
        values.add(grid[i][j])

values = sorted(values)

for low in values:
    ######### DP 배열 정리
    dp = [[INF] * n for _ in range(n)] ## max값만 저장

    dp[0][0] = grid[0][0] if grid[0][0] >= low else dp[0][0]

    ### 초기값
    for i in range(1, n):

        if dp[0][i-1] != INF: ####### 이전칸이 이동 가능했으면.
            dp[0][i] = max(dp[0][i-1], grid[0][i]) if grid[0][i] >= low else dp[0][i]
        if dp[i-1][0] != INF:
            dp[i][0] = max(dp[i-1][0], grid[i][0]) if grid[i][0] >= low else dp[i][0]
    

    for r in range(1, n):
        for c in range(1, n):
            if grid[r][c] < low: ## 현재칸이 INF보다 작으면
                continue

            ####### 둘다 이동 불가능
            if dp[r][c-1] == INF and dp[r-1][c] == INF:
                continue

            prev = min(dp[r-1][c], dp[r][c-1])

            # if dp[r][c-1] == INF: # 이전칸이 이동 불가능 했으면.
            #     dp[r][c] = max(prev, grid[r][c])
            # elif dp[r-1][c] == INF:
            #     dp[r][c] = max(prev, grid[r][c])
            # else:
            dp[r][c] = max(prev, grid[r][c])

    answer = min(answer, dp[n-1][n-1] - low)

print(answer)




















# INF = float('inf')

# answer = INF

# for row in grid:
#     for x in row:
#         values.add(x)

# # ==========================================
# # 경로의 최솟값 후보를 하나 고정
# # ==========================================
# for low in values:

#     # dp[i][j]
#     # =
#     # low보다 작은 칸을 밟지 않고
#     # (i,j)까지 왔을 때
#     # 가능한 "경로 최댓값"의 최소
#     dp = [[INF] * n for _ in range(n)]


#     # 시작점부터 low보다 작으면
#     # 이 low로는 경로를 만들 수 없음
#     if grid[0][0] < low:
#         continue


#     # 시작점
#     dp[0][0] = grid[0][0]


#     # ======================================
#     # 첫 번째 행
#     # ======================================
#     for j in range(1, n):

#         # 현재 칸이 low보다 작으면 못 지나감
#         if grid[0][j] < low:
#             continue

#         # 이전 칸까지 도달할 수 있었다면
#         if dp[0][j-1] != INF:
#             dp[0][j] = max(
#                 dp[0][j-1],
#                 grid[0][j]
#             )


#     # ======================================
#     # 첫 번째 열
#     # ======================================
#     for i in range(1, n):

#         if grid[i][0] < low:
#             continue

#         if dp[i-1][0] != INF:
#             dp[i][0] = max(
#                 dp[i-1][0],
#                 grid[i][0]
#             )


#     # ======================================
#     # 내부 DP
#     # ======================================
#     for i in range(1, n):
#         for j in range(1, n):

#             # low보다 작은 값은 사용 불가
#             if grid[i][j] < low:
#                 continue

#             # 위 / 왼쪽 중
#             # 경로 최댓값이 더 작은 쪽 선택
#             prev = min(
#                 dp[i-1][j],
#                 dp[i][j-1]
#             )

#             # 둘 다 못 오는 경우
#             if prev == INF:
#                 continue

#             # 현재 칸을 포함한 경로 최댓값
#             dp[i][j] = max(
#                 prev,
#                 grid[i][j]
#             )


#     # 도착할 수 있다면
#     if dp[n-1][n-1] != INF:

#         high = dp[n-1][n-1]

#         # 경로의 최댓값 - 최솟값 후보
#         answer = min(
#             answer,
#             high - low
#         )


# print(answer)