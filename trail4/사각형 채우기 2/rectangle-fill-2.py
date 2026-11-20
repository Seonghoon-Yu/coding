n = int(input())

# Please write your code here.


## 배열 정의
dp = [0] * max(3,(n+1))


## 점화식
# 현재 i state에 도달하기 이전의 상태

### i-1 -> l 하나 -> 1
### i-2 -> ll (제외), ㅡㅡ, ㅁ -> 2
### i-3 -> ㄴ


## 초깃값
dp[0] = 1
dp[1] = 1
dp[2] = 3

## 구현

for i in range(2, n+1):
    dp[i] = (dp[i-1] + 2*dp[i-2]) % 10007


print(dp[n])

