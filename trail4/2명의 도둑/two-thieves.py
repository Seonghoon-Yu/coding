n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## 2명의 도둑
## NxN
## 연속한 M개의 열에 있는 물건들을 훔침.
## 각각 최대무개 C, 합이 C를 넘으면안됌.
## C가 넘으면 그중에 적절하게 고름.
## 가치는 W*W

#####
# 두명의 도둑 좌표 완전 탐색.
# M 길이 무게 계산, C 초과하는지 확인, C내에서 최고 가지.


#### 전체 좌표에서 M길이 골랐을떄의 최대 가치.
#### 여기서 도둑의 좌표 완전 탐색.

def dfs(index, total):
    global max_value


    value = 0
    if sum(total) <= c:
        for t in total:
            value += t*t
    max_value = max(max_value, value)

    for i in range(index, len(selected)):
        total.append(selected[i])
        dfs(i+1, total)
        total.pop()




profit = [[0]*(n-m+1) for _ in range(n)]

for i in range(n):
    for j in range(n-m+1):
        ## 해당 M 구간 weight 가져오기
        ## C보다 높은지 확인
        ## weight의 가능한 조합에서 maximum profit 계산

        value = 0
        max_value = 0
        selected = weight[i][j:j+m]
        

        if sum(selected) > c:
            ##### 초과하는 경우 selected의 조합.
            dfs(0, [])
            value = max_value
        else:
            for s in selected:
                value += s*s
            
        profit[i][j] = value

## 두명 도둑 완전 탐색
max_profit = 0
for r1 in range(n):
    for c1 in range(n-m+1):
        for r2 in range(n):
            for c2 in range(n-m+1):
                if r1 == r2:
                    if c1+m > c2:
                        continue
                
                cur_profit = profit[r1][c1] + profit[r2][c2]
                max_profit = max(max_profit, cur_profit)

print(max_profit)