def subset_sum(input_set, target_sum):
    n = len(input_set)
    s = target_sum

    table = [[(True, []) if j == 0 else (False, []) for j in range(s+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, s+1):
            if input_set[i-1] <= j:
                include_result = (table[i-1][j-input_set[i-1]][0], table[i-1][j-input_set[i-1]][1] + [input_set[i-1]])
                exclude_result = table[i-1][j]
                if include_result[0]:
                    table[i][j] = include_result
                else:
                    table[i][j] = exclude_result
            else:
                table[i][j] = table[i-1][j]

    return table[n][s]

print(subset_sum([2,3,5,9,4], 12))

    
    