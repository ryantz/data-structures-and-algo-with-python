def linear_search(arr, key):
    for a in arr:
        if a == key:
            return True
            #return arr.index("needle")
        
    return False
        

haystack = ["no", "needle1", "yes", "hello", 3, "ray", "needle", 4, 1, 4 ,"ok"]
needle = "needle"

print(linear_search(haystack, needle))