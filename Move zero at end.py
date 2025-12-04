def move_zeros_inplace(arr):
    index = 0  # pointer for non-zero elements
    
    for num in arr:
        if num != 0:
            arr[index] = num
            index += 1
    
    # Fill remaining positions with zeros
    while index < len(arr):
        arr[index] = 0
        index += 1

    return arr

# Example
arr = [0, 1, 0, 3, 12]
print(move_zeros_inplace(arr))   # Output: [1, 3, 12, 0, 0]