def sum_of_differences(arr):
    # If the array is empty or has only one element, return 0
    if len(arr) < 2:
        return 0
    
    # Sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # Compute the sum of differences between consecutive elements
    total_difference = 0
    for i in range(len(sorted_arr) - 1):
        total_difference += sorted_arr[i] - sorted_arr[i + 1]
    
    return total_difference