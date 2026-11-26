n = int(input())

# Please write your code here.
# n =10

# DP 배열 정리
dp = [0] * max(3, n+2)

# DP 초기값
dp[0] = 1 ########?
dp[1] = 2
dp[2] = 7
# dp[3] = 2 * dp[2] + 3 dp[1] + 

# 점화식
'''
## N - 1 
l or ㅁㅁ

## N - 2
ㅡㅡ , ㅁㅁ ㅡ or ㅡ ㅁㅁ

## N - 3
ㅁ ㅡ
ㅡ ㅁ 2개

## N - 4
ㅁ ㅡ ㅡ ㅁ
ㅡ ㅡ ㅡ ㅡ

## N - 5
ㅁ ㅡ ㅡ
ㅡ ㅡ ㅁ 2개


'''

# 구현

for i in range(3, n+1):
    # print('i', i)
    # print('sum', sum([2 * dp[j] for j in range(i, 1, -2)]))
    # print('sum', 2 * dp[i-1] + 3 * dp[i-2])
    dp[i] = 2 * dp[i-1] + 3 * dp[i-2] + 2* sum(dp[:i-2])
    dp[i] %= 1_000_000_007



print(dp[n])