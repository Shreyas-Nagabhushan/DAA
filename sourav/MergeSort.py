inversions = 0

def merge(a1, a2):
    global inversions

    res = []
    i = 0
    j = 0

    while i <len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            res.append(a1[i])
            i+=1
        else:
            inversions += len(a1) - i
            res.append(a2[j])
            j+=1
    
    while i < len(a1):
        res.append(a1[i])
        i+=1
    while j < len(a2):
        res.append(a2[j])
        j+=1
    
    return res

def merge_sort(a):
    if len(a) <= 1:
        return a
    return merge(merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:]))

n = int(input("Enter the number of elements: "))
res = merge_sort([int(input(f"Enter element {i+1}: ")) for i in range(n)])

print("Sorted Array: ", res)
print("Number of inversions: ", inversions)