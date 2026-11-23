n = int(input())
N = n
# Please write your code here.


## 우선 수열 구하기


def sequence(seq):
    for size in range(1, len(seq)//2+1):
            # 0:1
            # 1:2

        cur_seq = seq[len(seq)-size:]
        next_seq = seq[len(seq)-size-size:len(seq)-size]
        
        # cur_seq_str = ''
        # next_seq_str = ''
        # for c, n in zip(cur_seq, next_seq):
        #     # print(c)
        #     c = str(c)
        #     n = str(n)
        #     cur_seq_str += c
        #     next_seq_str += n
        # # print(cur_seq_str)

        if cur_seq == next_seq:
            return False

    return True

# print(sequence([1,1,1,1]))

# possible_total = []

def dfs(total):
    # if not sequence(total):
    #     return
    
    if total:
        if len(total) == N:
            if sequence(total):
                print(''.join(map(str, total)))
            return True
    
    for i in range(4, 6+1):


        total.append(i)
        if sequence(total):
            if dfs(total):
                return True
        total.pop()

    return False

dfs([])