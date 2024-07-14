def get_input():
    n = int(input('Number of items: '))
    items = [-1] * (n+1) 
    for i in range(1, len(items)):
        value = int(input('Value: '))
        weight = int(input('Weight: '))
        items[i] = [value, weight]
    return items

def knapsack(items, capacity):
    #items is 1 indexed
    m = len(items)
    dp = [[0 for _ in range(capacity+1)] for _ in range(m)]

    for i in range(1, m):
        for weight in range(capacity+1):
            #take or not take
            take = not_take = -float('inf')

            not_take = dp[i-1][weight]

            if items[i][1] <= weight:
                take = items[i][0] + dp[i-1][weight - items[i][1]] 

            dp[i][weight] = max(not_take, take)
    
    for row in dp:
        print(row)

    chosen = [] 

    def find_solution(i, w):
        if i < 1 or w <= 0 :
            return 
        if dp[i][w] > dp[i-1][w]:
            chosen.append(i)
            find_solution(i-1, w-items[i][1])
        else:
            find_solution(i-1, w)

    find_solution(len(items)-1, capacity)
    print(chosen)

items = get_input()
capacity = int(input('Enter capacity: '))
knapsack(items, capacity)

