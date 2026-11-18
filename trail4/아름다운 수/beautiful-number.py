n = int(input())

# Please write your code here.

##### 1~4 범위 N자리 정수
#### 모든 가능한 조합부터 생성
#### 1 1번 연속
### 2 2번 연속
### 3 3번 연속

### dfs로 모든 가능한 조합 만들기?

### 아름다운 수 체크는 어떻게?

def beutiful(nums):
    
    len_nums = len(nums)
    
    i = 0

    while i < len_nums:
        # print(i)
        cur_num = nums[i]
        
        # print('cur_num', cur_num)

        if (i+cur_num-1) >= len_nums: ## 다음에 숫자가 없음
            return False

        count = 0
        ## 현재부터 다음 cur_num 까지 확인
        for j in range(i, i+cur_num):
            next_num = nums[j]
            
            if cur_num != next_num:
                return False
            else:
                count += 1
            
        if count != cur_num:
            return False
            
        i += cur_num

    return True


# print(beutiful([1,2,2,3,3,3]))


answer = 0
def dfs(total, count):
    global answer
    if count == n:
        answer += beutiful(total)
        return

    for j in range(1, 5):

        total.append(j)
        dfs(total, count+1)
        total.pop()

dfs([],0)

print(answer)