def merge(a, b):
    l1 = len(a)
    l2 = len(b)
    i = j = 0
    result = []
    while i < l1 and j < l2:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:]
    result += b[j:]
    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    first = arr[:m]
    second = arr[m:]
    first = mergesort(first)
    second = mergesort(second)
    return merge(first, second)

arr = [5,3,7,4,9,1]
print(mergesort(arr))