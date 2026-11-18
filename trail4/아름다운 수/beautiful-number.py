n = int(input())

# Please write your code here.

##### 1~4 범위 N자리 정수
#### 모든 가능한 조합부터 생성
#### 1 1번 연속
### 2 2번 연속
### 3 3번 연속

### dfs로 모든 가능한 조합 만들기?

### 아름다운 수 체크는 어떻게?
# def is_beautiful():
#     i = 0

#     while i < n:
#         num = arr[i]

#         # num개를 확인할 공간이 부족
#         if i + num > n:
#             return False

#         # num개가 전부 num인지 확인
#         for j in range(i, i + num):
#             if arr[j] != num:
#                 return False


def beutiful(nums):
    i = 0

    while i < n:
        cur_num = nums[i]

        if i + cur_num > n:
            return False

        for j in range(i, i+cur_num):
            
            if cur_num != nums[j]:
                return False
    
        i += cur_num

    return True


# def beutiful(nums):
    
#     len_nums = len(nums)
    
#     i = 0

#     while i < len_nums:
#         # print(i)
#         cur_num = nums[i]
        
#         # print('cur_num', cur_num)

#         if (i+cur_num-1) >= len_nums: ## 다음에 숫자가 없음
#             return False

#         count = 0
#         ## 현재부터 다음 cur_num 까지 확인
#         for j in range(i, i+cur_num):
#             next_num = nums[j]
            
#             if cur_num != next_num:
#                 return False
#             else:
#                 count += 1
            
#         if count != cur_num:
#             return False
            
#         i += cur_num

#     return True


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