# compare first index with the next, if first > next, swap
# after first iter, last index is always the biggest
# no need to include last index into the next iteration
# algo stops after the whole array is sorted / left with one element

def bubble_sort(arr):

    for i in range(len(arr)-1): # access whole array
        for j in range(0, len(arr) - i - 1): # compare each element

            #swap array position
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


numbers = [10, 30, 20, 44, 55, 6]
bubble_sort(numbers)
print(numbers)
