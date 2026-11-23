n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.



## 가로줄 가능한 조합해서 결과와 같으면 기억.
## 최소가 되는 가로줄

## 1,1 이면 0, 1 바꿈

## edge sort
edges.sort(key=lambda x: (x[1], x[0]))
start = [_ + 1 for _ in range(n)]
# print(start)

def get_results(start, total):
    target = start[:]
    for e in total:
        # print(e)
        l = e[0] - 1

        target[l], target[l+1] = target[l+1], target[l]
    return target

target = get_results(start, edges)

# print(start, target)

#### 모든 가능한 edges의 조합

min_count = float('inf')
def dfs(index, total):
    global min_count

    if target == get_results(start, total):
        min_count = min(len(total), min_count)
    
    for i in range(index, len(edges)):
        total.append(edges[i])
        dfs(i+1, total)
        total.pop()

dfs(0,[])
print(min_count)
