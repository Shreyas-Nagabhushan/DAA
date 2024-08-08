class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
    def __repr__(self):
        return "Item: " + f"Profit: {self.profit} | Weight: {self.weight}"

n = int(input("Enter the number of items: "))
w = int(input("Enter the knapsack capacity: "))
items = [Item(int(input(f"Enter profit of item {i+1}: ")), int(input(f"Enter weight of item {i+1}: "))) for i in range(n)]

table = [[(0, []) for _ in range(w+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, w+1):
        exclude_profit = table[i-1][j][0]
        include_profit = items[i-1].profit +  table[i-1][j-items[i-1].weight][0]
        
        if items[i-1].weight <= j:
            if include_profit > exclude_profit:
                table[i][j] = (include_profit, table[i-1][j-items[i-1].weight][1] + [items[i-1]])
            else:
                table[i][j] = table[i-1][j]
        else:
            table[i][j] = table[i-1][j]

print(table[n][w])    

