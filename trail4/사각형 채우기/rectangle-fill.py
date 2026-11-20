n = int(input())

# Please write your code here.


## 2xN 크기의 사각형을 1x2, 2x1 크기의 사각형으로 채우는 방법의 수
# N=3 일떈 3

# 현재 상태 i 이전에 무엇

# N-1 이면 이전에서 가능
# N-2 이면 이전에서 가능

## DP 배열 정의
dp = [0] * (n+1)

## 초기값
if n >= 1:
    dp[1] = 1

if n >= 2:
    dp[2] = 2


for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])
