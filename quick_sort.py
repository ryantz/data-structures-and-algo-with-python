# trying to implement a quick sort 
# divide and conquer strategy 
# choose a pivot (last element)
# <= will be on the left of pivot
# > will be on the right of pivot

def partition(arr, lo, hi):
    pivot = arr[hi]
    idx = lo - 1 # pointer to the values in array

    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1 # increment pointer 
            # swap the positions
            temp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = temp

    # changing  pivot pointer so that it follows left right concept
    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot
    return idx
    

def quick_sort(arr, lo, hi):
    if lo >= hi:
        return
    else:
        # partition the list by adding pivots
        pivot_idx = partition(arr, lo, hi)
        # recursively sort the left and right
        quick_sort(arr, lo, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, hi)


sort_this = [3,6,4,1,9,0,8,7,10,5,2]
quick_sort(sort_this, 0, len(sort_this)-1)
print(sort_this)