def f(arr, i, sum_rem):
    if i < 0:
        return sum_rem == 0
    
    choose = False 
    not_choose = False

    not_choose = f(arr, i-1, sum_rem)
    if arr[i] <= sum_rem:
        choose = f(arr, i-1, sum_rem - arr[i])

    return not_choose or choose

def f_dp(arr, i, sum_rem, dp):
    if i < 0:
        return sum_rem == 0
    
    if dp[i][sum_rem] != -1:
        return dp[i][sum_rem] 
    
    choose = False 
    not_choose = False

    not_choose = f_dp(arr, i-1, sum_rem, dp)
    if arr[i] <= sum_rem:
        choose = f_dp(arr, i-1, sum_rem - arr[i], dp)

    dp[i][sum_rem] = choose or not_choose
    return dp[i][sum_rem]

def subset_tabular(arr, target):
    dp = [[0 for _ in range(target+1)] for _ in range(len(arr)+1)]

    for curr_index in range(1, len(dp)):
        for curr_target in range(1, len(dp[0])):
            choose = not_choose = 0 

            not_choose = dp[curr_index - 1][curr_target]

            if arr[curr_index - 1] <= curr_target:
                choose = arr[curr_index-1] + dp[curr_index - 1][curr_target - arr[curr_index - 1]]

            dp[curr_index][curr_target] = max(choose, not_choose)
    
    for row in dp:
        print(row)

    chosen_items = [] 

    def find_solution(curr_target, curr_index):
        if curr_target == 0:
            return 
        if dp[curr_index][curr_target] > dp[curr_index - 1][curr_target]:
            chosen_items.append(curr_index - 1)
            find_solution(curr_target-arr[curr_index-1], curr_index-1)
        else:
            find_solution(curr_target, curr_index-1)

    find_solution(target, len(dp)-1)
    print(chosen_items)


arr = [5,1,7,2]
target = 3
# dp = [[-1 for _ in range(target + 1)] for _ in range(len(arr))]
# print(f_dp(arr, len(arr)-1, 3, dp))
subset_tabular(arr, target)
# print(f(arr, len(arr)-1, 3))