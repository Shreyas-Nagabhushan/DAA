def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    lesser = [] 
    greater = []
    for i in range(1, len(arr)):
        item = arr[i]
        if item < pivot:
            lesser.append(item)
        else:
            greater.append(item)
    
    return quicksort(lesser) + [pivot] + quicksort(greater)
    
arr = [] 
n = int(input('Enter how many elements : '))
for _ in range(n):
    arr.append(int(input('Element: ')))

print('Sorted array: ')
print(quicksort(arr))
