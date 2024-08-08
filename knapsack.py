def knapsack(weights, profits, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    for i in range(1, n):
        for c in range(1, capacity+1):
            choose = not_choose = dp[i-1][c]
            if weights[i] <= c:
                choose = profits[i] + dp[i-1][c - weights[i]]
            
            dp[i][c] = max(choose, not_choose)
    
    r = n-1 
    c = capacity 
    items = [] 
    while r > 0:
        if dp[r][c] > dp[r-1][c]:
            items.append(r)
            c -= weights[r] 
        r -= 1 

    print(dp)
    print(items)

weights = [0, 3,5,6,2]
profits = [0, 10,4,9,11]
knapsack(weights, profits, 7)