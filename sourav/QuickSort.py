def QuickSort(a):
    if len(a)<=1:
        return a
    
    pivot = 0

    left = []
    right = []

    for i in range(len(a)):
        if i!= pivot:
            if a[i] < a[pivot]:
                left.append(a[i])
            else:
                right.append(a[i])
    
    return QuickSort(left) + [a[pivot]] + QuickSort(right)

n = int(input("Enter the number of elements: "))
res = QuickSort([int(input(f"Enter element {i+1}: ")) for i in range(n)])

print("Sorted Array: ", res)
