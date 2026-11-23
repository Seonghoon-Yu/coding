import sys
sys.setrecursionlimit(10**6)
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

## 1번부터 M 번까지 1차원 윳놀이
## K개의 말이 1번 지점.
# N번의 턴, N번 전진
# 각 턴마다 하나의 말 선택하여 해당 수 만큼 앞으로 나아감.
# M번에 도달하면 1점
# M번에 도달한 말을 또 선택할 수는 있지만, 아무런 변화 X

# N번 해서 얻을 수있는 점수중 최댓값.


# 우선은 1~M 고정
# K개 말 시작지점 고정
# N이 달라지는데 N에 따라 K개 선택하는 모든 경우의 수

board = [_+1 for _ in range(m)]

horse = [1 for _ in range(k)]


max_count = 0
def dfs(index):
    global max_count

    if index >= len(nums):
        # print(horse)
        count = sum([h >= m for h in horse])
        max_count = max(count, max_count)
        
        # print(any(h >= m for h in horse))
        return

    n = nums[index]

    for i in range(len(horse)):
        # if horse[i] >= m:
        #     continue
        horse[i] += n
        dfs(index+1)
        horse[i] -= n

dfs(0)

print(max_count)