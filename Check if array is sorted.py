def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return false
        return True
arr=[1,2,3,4,5]
if is_sorted(arr):
    print("array is sorted")
else:
     print("array is not sorted")