n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]


####### 모든 가능한 2개의 M 구간 조합

possible_coord = []

for r1 in range(n):
    for c1 in range(n-m+1): ## range에서 구간 조절
        for r2 in range(n):

            if r1 != r2:
                for c2 in range(n-m+1):
                    possible_coord.append([(r1, c1), (r2, c2)])

            else:
                for c2 in range(c1+m, n-m+1):
                    possible_coord.append([(r1, c1), (r2, c2)])

####### 2개의 각 M 구간에 해당하는 weight 가져오기
def get_weight(coord):
    x, y = coord
    cur_weight = [weight[x][y+i] for i in range(m)]

    return cur_weight
    # return


def dfs(index, collected, total_weight):
    global dfs_max


    if collected:
        collected_value = sum([w*w for w in collected])
        if sum(collected) <= c:
            dfs_max = max(dfs_max, collected_value)

    if index >= m:
        return
    

    for i in range(index,m):
        collected.append(total_weight[i])
        dfs(i+1, collected, total_weight)
        collected.pop()


max_value=0

### 가능한 coord 조합 완전 탐색
for i in range(len(possible_coord)):
    cur_coord = possible_coord[i]
    weight1, weight2 = get_weight(cur_coord[0]), get_weight(cur_coord[1])
    value1, value2 = sum([w*w for w in weight1]), sum([w*w for w in weight2])

    if sum(weight1) <= c:
        final_value1 = value1
    else:
        dfs_max = 0
        dfs(0, [], weight1)
        final_value1 = dfs_max

    if sum(weight2) <= c:
        final_value2 = value2
    else:
        dfs_max = 0
        dfs(0, [], weight2)
        final_value2= dfs_max

    total_value = final_value1 + final_value2
    max_value = max(max_value, total_value)

print(max_value)




## 합이 c 이상, 이하 계산

### 이상일시 dfs
