# code
def buildHeap(arr):
    n = len(arr)
    
    if n == 0 or n == 1:
        return arr
    
    res = [arr[0]]
    for i in range(1, n):
        child = i
        res.append(arr[child])
        parent = (i - 1) // 2
        
        while res[parent] < res[child] and parent >= 0 and child >= 0:
            res[parent], res[child] = res[child], res[parent]
            child = parent
            parent = (child - 1) // 2
    
    return res

def mergeHeap(arr1, arr2):
    res = arr1 + arr2
    res.sort()  # Merge and sort the two arrays
    
    return buildHeap(res)

# Example usage:
arr1 = [3, 1, 4]
arr2 = [2, 6, 5]
result = mergeHeap(arr1, arr2)
print(result)

# question link
# https://www.codingninjas.com/studio/problems/merge-two-binary-max-heaps_1170049