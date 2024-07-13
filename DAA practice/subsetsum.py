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


arr = [5,2,7,2]
target = 3
dp = [[-1 for _ in range(target + 1)] for _ in range(len(arr))]
print(f_dp(arr, len(arr)-1, 3, dp))

print(f(arr, len(arr)-1, 3))