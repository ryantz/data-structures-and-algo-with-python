# find mid point, adjust pointer accordingly

def binary_search(arr, n):
    start = 0
    end = len(arr) - 1
    mid = 0

    while start <= end:
        mid = (start + end )// 2
        
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            start = mid + 1
        else:
            end = mid

haystack = [1, 2, 3, 4, 5, 6, 7]
needle = 3

result = binary_search(haystack, needle)
print(result)